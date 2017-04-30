#import Drivers.ServoSG90
from MsgServo import *
from Drivers.ServoEnums import *
from enum import Enum
import logging

class ServoFactory(object):
    """description of class"""
    log = logging.getLogger('SemBrain')

    def __init__(self):
        ServoFactory.log.info('ServoFactory.init')

    def OpenServo(self, servo):
        ServoFactory.log.info("Opening servo {0}".format(servo))
        if(servo.strip().lower() == "E1".strip().lower()):
            #Servo_E1 = Drivers.ServoSG90.ServoSG90(23, 50, 2.5, 11.5, 0, 180)
            Servo_E1.SetAngle(180)
            Servo_E1.Stop()
        elif(servo.strip().lower() == "L1".strip().lower()):
            #Servo_L1 = Drivers.ServoSG90.ServoSG90(22, 50, 2.5, 11.5, 0, 180)
            Servo_L1.SetAngle(180)
            Servo_L1.Stop()

    def CloseServo(self, servo):
        ServoFactory.log.info("Closing servo {0}".format(servo))
        if(servo.strip().lower() == "E1".strip().lower()):
            #Servo_E1 = Drivers.ServoSG90.ServoSG90(23, 50, 2.5, 11.5, 0, 180)
            Servo_E1.SetAngle(0)
            Servo_E1.Stop()
        elif(servo.strip().lower() == "L1".strip().lower()):
            #Servo_L1 = Drivers.ServoSG90.ServoSG90(22, 50, 2.5, 11.5, 0, 180)
            Servo_L1.SetAngle(0)
            Servo_L1.Stop()

    def ExecuteCommand(self, cmd):
        print ("execute cmd")
        ServoFactory.log.info("trying to execute command")
        if(isinstance(cmd, MsgElServo) == False):
            return False
        ServoFactory.log.info("Pass 1")
        if(cmd.Action == ServoAction.Open):
            self.OpenServo(cmd.Servo)
        elif(cmd.Action == ServoAction.Close):
            self.CloseServo(cmd.Servo)
        elif(cmd.Action == ServoAction.ServoReset):
            self.CloseServo("E1")
            self.CloseServo("L1")
        elif(cmd.Action == ServoAction.ServoClear):
            self.OpenServo("E1")
            self.OpenServo("L1")
        ServoFactory.log.info("Pass 2")





