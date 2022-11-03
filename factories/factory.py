from dialer_plus_pro.dialer_pro import DialerPro
from services.dialer_pro_adapter import DialerProAdapter
from services.power_dialer import PowerDialer


class Factory:

    @staticmethod
    def create_power_dialer() -> PowerDialer:
        return PowerDialer()

    @staticmethod
    def create_dialer_plus_pro_adapter() -> DialerProAdapter:
        return DialerProAdapter(DialerPro())
