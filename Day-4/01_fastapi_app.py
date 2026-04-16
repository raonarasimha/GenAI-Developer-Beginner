from fastapi import FastAPI, Request
import uvicorn

class GenAIChatBot:
    def ask(self, prompt):
        return f"[Mocked OpenAI reply to: '{prompt}']"

app = FastAPI()

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    response = GenAIChatBot().ask(data["prompt"])
    return {"response": response}

@app.get("/hello")
async def chat(req: Request):
    return {"response": "hello world!"}

if __name__ == "__main__":
    print("Run with: uvicorn 01_fastapi_app:app --reload")
