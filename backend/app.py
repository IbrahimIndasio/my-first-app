"""AI Live System FastAPI application.

Exposes a simple root endpoint that reports application liveness.
Intended to run on port 10000 (configured in the uvicorn entrypoint below).
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("../frontend/index.html")

@app.get("/hello")
def hello():
    return {"message": "Hello from my first live API"}


if __name__ == "__main__":
    # Local dev entrypoint. Render will use the same command in render.yaml.
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
