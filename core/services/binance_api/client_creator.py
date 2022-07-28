from core.services.binance_api.spot_api import SpotClient


def create_spot_client() -> SpotClient:
    return SpotClient()
