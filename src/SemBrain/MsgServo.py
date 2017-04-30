from Drivers.ServoEnums import *

class MsgElServo(object):
    """description of class"""

    def __init__(self, name, action, servo):
        self.Name = name
        self.Servo = servo
        self.Action = action

    def __str__(self):
        return "Cmd: {0} {1} >>{2}".format(self.Name, self.Action, self.Servo)


