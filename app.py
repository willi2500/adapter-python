import asyncio

from factories.factory import Factory
from services.dialer_service import DialerService


async def main():
    print("inicio de app")

    # await DialerService(Factory.create_power_dialer()).run()
    await DialerService(Factory.create_dialer_plus_pro_adapter()).run()

if __name__ == "__main__":
    asyncio.run(main())
