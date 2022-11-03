from __future__ import annotations


class User:
    id: str
    number: str

    def __init__(self, id: str | None = None, number: str | None = None):
        self.id = id
        self.number = number

    @classmethod
    def init_with_id(cls, id: str) -> User:
        return cls(id=id)

    @classmethod
    def init_with_id_number(cls, id: str, number: str) -> User:
        return cls(id=id, number=number)
