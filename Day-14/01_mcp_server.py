"""
Minimal MCP-like stdio server (mock) exposing two tools:
- list_dir: list files in Day-14/assets
- read_text: read a .txt file from Day-14/assets

This is a simplified placeholder to demonstrate the flow without requiring
external MCP packages. It reads JSON lines from stdin and writes JSON lines to stdout.
"""

import os
import sys
import json

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def list_dir() -> dict:
    items = []
    for name in os.listdir(ASSETS_DIR):
        items.append({"name": name})
    return {"files": items}


def read_text(filename: str) -> dict:
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.abspath(path).startswith(os.path.abspath(ASSETS_DIR)):
        return {"error": "Forbidden path"}
    if not os.path.isfile(path) or not filename.lower().endswith('.txt'):
        return {"error": "File not found or not a .txt"}
    with open(path, 'r', encoding='utf-8') as f:
        return {"content": f.read()}


def handle_request(obj: dict) -> dict:
    method = obj.get("method")
    params = obj.get("params", {})
    if method == "list_dir":
        return {"ok": True, "result": list_dir()}
    if method == "read_text":
        filename = params.get("filename", "")
        return {"ok": True, "result": read_text(filename)}
    return {"ok": False, "error": "Unknown method"}


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
        except Exception as e:
            resp = {"ok": False, "error": str(e)}
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()


