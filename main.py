from app import create_app
import uvicorn

app = create_app()

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000)