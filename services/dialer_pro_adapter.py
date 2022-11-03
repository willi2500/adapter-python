from dialer_plus_pro.dialer_pro import DialerPro
from dialer_plus_pro.infocall import InfoCall
from models.call_data import CallData
from models.user import User
from services.dialer import Dialer


class DialerProAdapter(Dialer):
    __dialer_plus_pro: DialerPro
    __info_call: InfoCall

    def __init__(self, dialer_plus_pro: DialerPro):
        self.__dialer_plus_pro = dialer_plus_pro

    async def make_call(self, user: User) -> CallData:
        self.__info_call = self.__dialer_plus_pro.dial(user)
        return CallData()

    async def send_message(self, call_data: CallData) -> None:
        self.__dialer_plus_pro.play_message(self.__info_call)

    async def hangup(self, call_data: CallData) -> None:
        self.__dialer_plus_pro.hang_up(self.__info_call)
