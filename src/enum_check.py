from enum import Enum


class Days(Enum):
    Sun = ("1", "sunday")
    Mon = ("2", "Monday")
    def __init__(self, keyId, val):
        self.keyId = keyId
        self.val = val

    @property
    def value(self):
        return self.val

    @property
    def key(self):
        return self.key


print(Days.Mon.keyId)

