# ai-live-system

FastAPI service that reports liveness at the root endpoint and is ready for deployment on Render.

## Quick start (local)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   uvicorn backend.app:app --host 0.0.0.0 --port 10000 --reload
   ```
3. Visit `http://localhost:10000/` to see `AI System Live`.

## Deployment on Render
Render reads `render.yaml` to set up the service:
- Build: `pip install -r requirements.txt`
- Start: `uvicorn backend.app:app --host 0.0.0.0 --port 10000`
- Python version: 3.11

To deploy:
1. Push this repo to GitHub.
2. In Render, create a new Web Service from the repo; Render will pick up `render.yaml`.
3. Once deployed, the homepage returns `AI System Live` on port 10000.
