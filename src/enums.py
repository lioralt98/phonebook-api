from enum import Enum


class PhoneNumberTypesEnum(str, Enum):
    MOBILE = "mobile"
    HOME = "home"
    WORK = "work"
    NONE = "none"
    
    @classmethod
    def contains(cls, v: str):
        return any(v == i.value for i in cls)
    
