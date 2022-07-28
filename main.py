from fastapi import FastAPI

from core.models.get_token_price_base_model import GetTokenPrice
from core.services.binance_api.client_creator import create_spot_client

app = FastAPI()


@app.post("/get_token_price")
def read_root(get_token_price_base_model: GetTokenPrice):
    token = get_token_price_base_model.token
    return create_spot_client().get_token_price(token)
