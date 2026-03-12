"""AI Live System FastAPI application.

Exposes a simple root endpoint that reports application liveness.
Intended to run on port 10000 (configured in the uvicorn entrypoint below).
"""

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="ai-live-system")


@app.get("/", response_class=PlainTextResponse, summary="Service liveness")
async def root() -> str:
    """Return a plaintext heartbeat to indicate the service is healthy."""
    return "AI System Live"


if __name__ == "__main__":
    # Local dev entrypoint. Render will use the same command in render.yaml.
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
