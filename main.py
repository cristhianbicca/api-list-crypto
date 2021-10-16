import os
from typing import Optional
from fastapi import FastAPI
import requests
from .connect import get_response

app = FastAPI()

api_url = "https://www.mercadobitcoin.net/api/"


@app.get("/crypto/{crypto_coin}")
def get_quote(crypto_coin: str, method: str):
    response = get_response(api_url, crypto_coin, method)
    return response
