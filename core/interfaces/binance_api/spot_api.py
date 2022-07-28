import abc


class ISpotClient(abc.ABC):
    @abc.abstractmethod
    def get_token_price(self, token: str):
        raise NotImplementedError
