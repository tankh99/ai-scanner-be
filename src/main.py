import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from db import read_value, write_value
import json

load_dotenv()

app = FastAPI()
host = os.environ.get("HOST", "0.0.0.0")
port = os.environ.get("PORT", 8080)


@app.get("/get_current_designer")
def get_current_designer():
    return read_value()

class DesignerPayload(BaseModel):
    name: str
    outfit_url: str

@app.post("/update_current_designer")
def update_current_designer(payload: DesignerPayload):
    write_value(payload)

if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port, reload=True)