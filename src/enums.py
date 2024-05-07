from enum import Enum


class PhoneNumberTypesEnum(str, Enum):
    MOBILE = "mobile"
    HOME = "home"
    WORK = "work"
    NONE = "none"
    
