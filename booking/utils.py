from enum import IntEnum

class ServiceType(IntEnum):
    PAMPER_PACKAGE = 1
    FULL_GROOM = 2
    HAND_STRIP = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]