from models.user import User
from models.call_data import CallData
from services.dialer import Dialer
from utils.time_tool import Util


class PowerDialer(Dialer):
    async def make_call(self, user: User) -> CallData:
        print("realizando la llamada ....")
        await Util.sleep()
        return CallData()

    async def send_message(self, call_data: CallData) -> None:
        await Util.sleep()

    async def hangup(self, call_data: CallData) -> None:
        print("Cortando la llamada ....")
        await Util.sleep()
