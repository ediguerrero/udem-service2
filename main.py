from typing import Union

from fastapi import FastAPI
import requests
import logging
from requests.exceptions import HTTPError
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        ## logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
app = FastAPI()


@app.get("/authUsers/{internalId}")
def read_item(internalId: str):
    try:
        url = 'https://62fc4666abd610251c17fdae.mockapi.io/api/authUsers?internalId=' + internalId
        response = requests.get(url, {}, timeout=5)
        response.raise_for_status()
        jsonResponse = response.json()
        logging.info("getting info from authUsers service 2")
        if not jsonResponse:
            raise Exception("item not found")
        else:
            logging.info("item found")
        return {"items": jsonResponse}

    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'Other error occurred: {err}')
        return {"item not found"}
