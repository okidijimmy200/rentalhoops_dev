import api
from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

app.include_router(api.router, prefix="/api")




