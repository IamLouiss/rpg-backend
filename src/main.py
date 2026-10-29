from fastapi import FastAPI

app = FastAPI(
    title="RPG Adventure API",
    description="Backend for a professional RPG portfolio project.",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    """
    Endpoint to verify the API is up and running.
    """
    return {"status": "ok", "message": "The RPG Backend is alive!"}