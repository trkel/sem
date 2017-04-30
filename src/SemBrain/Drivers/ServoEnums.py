from enum import Enum

class ServoAction(Enum):
    Open = 180,
    Close = 0,
    ServoSet = 3,
    ServoClear = 4