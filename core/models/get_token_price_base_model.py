from pydantic.main import BaseModel


class GetTokenPrice(BaseModel):
    token: str
