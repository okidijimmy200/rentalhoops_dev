from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is the delivery platform backend."}
