from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/authUsers/{internalId}")
def read_item(internalId: str):
    url = 'https://62fc4666abd610251c17fdae.mockapi.io/api/authUsers?internalId='+internalId
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json()}
