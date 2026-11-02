"""FastAPI front door for the triage agent."""
from fastapi import FastAPI

app = FastAPI(title="ticket-triage-agent")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
