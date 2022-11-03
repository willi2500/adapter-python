import time

from dialer_plus_pro.infocall import InfoCall
from dialer_plus_pro.user import User


class DialerPro:

    @staticmethod
    def dial(dial_user: User) -> InfoCall:
        print("Start dialling....")
        time.sleep(3)
        return InfoCall()

    @staticmethod
    def play_message(info_call: InfoCall) -> InfoCall:
        print("Start playing message....")
        time.sleep(3)
        return InfoCall()

    @staticmethod
    def hang_up(info_call: InfoCall) -> InfoCall:
        print("Start hanging up")
        time.sleep(3)
        return InfoCall()
