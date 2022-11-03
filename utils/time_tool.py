import asyncio
from datetime import datetime, timedelta

from services.runnable import Runnable


class Util:

    @staticmethod
    async def sleep() -> None:
        await asyncio.sleep(1)

    @staticmethod
    def time_ellapsed(title: str, runnable: Runnable):
        print(f"Tomando tiempo de: {title}")
        time_before: datetime = datetime.now()
        runnable.run()
        time_after: datetime = datetime.now()
        time_difference: timedelta = (time_after - time_before)
        time_difference_microseconds: int = time_difference.microseconds
        print(f"Esto tarda... {time_difference_microseconds} ms")
