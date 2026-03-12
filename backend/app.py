"""AI Live System FastAPI application.

Exposes a simple root endpoint that reports application liveness.
Intended to run on port 10000 (configured in the uvicorn entrypoint below).
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_FILE = os.path.join(BASE_DIR, "frontend", "index.html")

client = OpenAI(api_key=os.getenv("6e25fbbe5262855092311f27375fd775"))

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def home():
    return FileResponse(INDEX_FILE)

@app.post("/ask")
def ask_ai(data: Prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=data.prompt
    )
    return {"answer": response.output[0].content[0].text}


if __name__ == "__main__":
    # Local dev entrypoint. Render will use the same command in render.yaml.
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
