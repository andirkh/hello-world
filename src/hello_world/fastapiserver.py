import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return "Hello World from FastAPI!"

def run_fastapi() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)
    