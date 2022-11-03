import math
import random

from models.user import User
from services.dialer import Dialer
from services.runnable import Runnable
from utils.time_tool import Util


class DialerService(Runnable):
    __dialer: Dialer

    def __init__(self, dialer: Dialer):
        self.__dialer = dialer

    async def run(self) -> None:
        while True:
            random_value: int = math.trunc(random.random() * 10)
            print(random_value)
            if random_value == 0:
                print(f"Si es 0 entonces NO realizar la llamada...")
                continue

            call_data = await self.__dialer.make_call(User())
            if random_value == 1:
                print("retrazar el llamado a emitir mensaje x q corresponde a la emrpes Arcor")
                await Util.sleep()

            await self.__dialer.send_message(call_data)

            if random_value == 2:
                print("Cortar 2 veces x que hay un bug")
                await self.__dialer.hangup(call_data)

            await self.__dialer.hangup(call_data)

            print("")
