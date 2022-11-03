import datetime


class InfoCall:
    id: str
    init_time: datetime
    duration: int

    def __init__(self, id: str = None, init_time: datetime = None, duration: int = None):
        self.id = id
        self.init_time = init_time
        self.duration = duration
