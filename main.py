from fastapi import FastAPI, HTTPException
from requests_oauthlib import OAuth1
import requests
import os

app = FastAPI()

BRICKLINK_BASE_URL = "https://api.bricklink.com/api/store/v1"
ALLOWED_TYPES = {"PART", "FIG", "MINIFIG"}


def bricklink_auth() -> OAuth1:
    return OAuth1(
        os.environ["CONSUMER_KEY"],
        os.environ["CONSUMER_SECRET"],
        os.environ["TOKEN"],
        os.environ["TOKEN_SECRET"],
        signature_method="HMAC-SHA1"
    )


def bricklink_get(url: str, params: dict | None = None):
    r = requests.get(
        url,
        auth=bricklink_auth(),
        params=params,
        timeout=15
    )

    if not r.ok:
        raise HTTPException(
            status_code=r.status_code,
            detail=r.text
        )

    return r.json()


def validate_type(item_type: str) -> str:
    item_type = item_type.upper()
    if item_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="item_type must be PART or FIG"
        )
    # exception
    if item_type == "FIG":
        item_type = "MINIFIG"
    return item_type


@app.get("/price/{item_type}/{item_id}")
def get_price(item_type: str, item_id: str):
    item_type = validate_type(item_type)

    return bricklink_get(
        f"{BRICKLINK_BASE_URL}/items/{item_type}/{item_id}/price",
        params={
            "new_or_used": "N"
        }
    )


@app.get("/colors/{item_type}/{item_id}")
def get_colors(item_type: str, item_id: str):
    item_type = validate_type(item_type)

    return bricklink_get(
        f"{BRICKLINK_BASE_URL}/items/{item_type}/{item_id}/colors"
    )


@app.get("/color/{color_id}")
def check_color(color_id: int):
   
    if color_id <= 0:
        raise HTTPException(status_code=400, detail="Color id must be > 0")

    return bricklink_get(
        f"{BRICKLINK_BASE_URL}/colors/{color_id}"
    )