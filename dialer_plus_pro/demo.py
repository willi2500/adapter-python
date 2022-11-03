import asyncio

from dialer_plus_pro.dialer_pro import DialerPro
from dialer_plus_pro.infocall import InfoCall
from dialer_plus_pro.user import User
from services.runnable import Runnable


class Demo(Runnable):

    async def run(self):
        info_call: InfoCall = DialerPro.dial(User())
        DialerPro.play_message(info_call)
        DialerPro.hang_up(info_call)


async def main():
    demo = Demo()

    await demo.run()


if __name__ == '__main__':
    asyncio.run(main())
