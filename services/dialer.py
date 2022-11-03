from abc import ABC, abstractmethod

from models.user import User
from models.call_data import CallData


class Dialer(ABC):

    @abstractmethod
    async def make_call(self, user: User) -> CallData:
        pass

    @abstractmethod
    async def send_message(self, call_data: CallData) -> None:
        pass

    @abstractmethod
    async def hangup(self, call_data: CallData) -> None:
        pass
