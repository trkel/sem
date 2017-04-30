import Drivers.ServoSG90
from MsgServo import *
from Drivers.ServoEnums import *
from enum import Enum

class ServoFactory(object):
    """description of class"""
    log = logging.getLogger('ServoFactory')

    def __init__(self):
        self.log = logging.getLogger('ServoFactory.init')


    def OpenServo(servo):
        if(trim(servo).strip().lower() == "E1".strip().lower()):
            Servo_E1 = ServoSG90.ServoSG90(23, 50, 2.5, 11.5, 0, 180)
            Servo_E1.SetAngle(180)
            Servo_E1.Stop()
        elif(trim(servo).strip().lower() == "L1".strip().lower()):
            Servo_L1 = ServoSG90.ServoSG90(22, 50, 2.5, 11.5, 0, 180)
            Servo_L1.SetAngle(180)
            Servo_L1.Stop()

    def CloseServo(servo):
        if(trim(servo).strip().lower() == "E1".strip().lower()):
            Servo_E1 = ServoSG90.ServoSG90(23, 50, 2.5, 11.5, 0, 180)
            Servo_E1.SetAngle(0)
            Servo_E1.Stop()
        elif(trim(servo).strip().lower() == "L1".strip().lower()):
            Servo_L1 = ServoSG90.ServoSG90(22, 50, 2.5, 11.5, 0, 180)
            Servo_L1.SetAngle(0)
            Servo_L1.Stop()

    def ExecuteCommand(self, cmd):
        if(isinstance(cmd, MsgServo) == False):
            return False

        if(cmd.Action == ServoAction.Open):
            OpenServo(cmd.Servo)
        elif(cmd.Action == ServoAction.Close):
            CloseServo(cmd.Servo)
        elif(cmd.Action == ServoAction.ServoSet):
            CloseServo("E1")
            CloseServo("L1")
        elif(cmd.Action == ServoAction.ServoClear):
            OpenServo("E1")
            OpenServo("L1")





