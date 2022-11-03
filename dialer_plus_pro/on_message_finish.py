from abc import ABC, abstractmethod

from dialer_plus_pro.infocall import InfoCall


class OnMessageFinish(ABC):

    @abstractmethod
    def accept(self, info_call: InfoCall) -> None:
        pass
