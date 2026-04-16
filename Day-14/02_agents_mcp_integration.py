"""
Agent + MCP (mock) integration demo.
This script spawns/assumes a running stdio server (01_mcp_server.py) and sends JSON requests via subprocess pipes.
Then it feeds the tool results into an LLM answer using OpenAI Responses API.
"""

import os
import json
import subprocess
from typing import Dict, Any

from dotenv import load_dotenv
from openai import OpenAI


def call_mcp(method: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Call the mock MCP server once (spawn per call for simplicity)."""
    cmd = ["python", os.path.join(os.path.dirname(__file__), "01_mcp_server.py")]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    req = {"method": method, "params": params or {}}
    assert proc.stdin and proc.stdout
    proc.stdin.write(json.dumps(req) + "\n")
    proc.stdin.flush()
    proc.stdin.close()
    line = proc.stdout.readline()
    proc.terminate()
    return json.loads(line)


def answer_with_tools(client: OpenAI, question: str, tool_payload: Dict[str, Any], model_name: str = "gpt-4o-mini") -> str:
    context = json.dumps(tool_payload, indent=2)
    messages = [
        {
            "role": "system",
            "content": "Use the following tool output to answer the user's question. If the answer is not apparent, say you don't know."
        },
        {
            "role": "user",
            "content": f"Tool Output:\n{context}\n\nQuestion: {question}\nAnswer:"
        }
    ]
    
    try:
        resp = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.2,
            max_tokens=1000
        )
        
        # Extract the response text
        if resp.choices and len(resp.choices) > 0:
            return resp.choices[0].message.content.strip()
        else:
            return "No response generated"
            
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    load_dotenv()
    
    # Check for OpenRouter configuration
    try:
        from openrouter_provider import create_openrouter_provider
        provider = create_openrouter_provider()
        client = provider.get_client()
        model_name = provider.get_model_name()
        print(f"✅ Using OpenRouter model: {model_name}")
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    except ImportError:
        print("Please install openai: pip install openai")
        return

    # 1) Call list_dir tool
    files_resp = call_mcp("list_dir")
    # 2) If a .txt is present, read its content
    filename = None
    if files_resp.get("ok"):
        for f in files_resp["result"].get("files", []):
            if f["name"].lower().endswith(".txt"):
                filename = f["name"]
                break
    text_resp = call_mcp("read_text", {"filename": filename}) if filename else {"ok": False, "error": "No .txt"}

    # 3) Ask LLM using tool output as context
    question = "Summarize the contents of the first text file."
    combined = {"files": files_resp, "content": text_resp}
    answer = answer_with_tools(client, question, combined, model_name)
    print("Q:", question)
    print("A:", answer)


if __name__ == "__main__":
    main()


