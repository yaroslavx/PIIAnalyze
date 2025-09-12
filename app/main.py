from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from utils import json_to_dict_list
import os
from typing import Optional

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')

@app.get("/")
def home_page():
    return {"message": "Hi everyone"}