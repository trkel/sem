from Drivers.BaseServo import *
import RPi.GPIO as GPIO
import time
import logging

class ServoSG90:
    """description of class"""
    log = logging.getLogger('ServoSG90')

    def __init__(self, pin, frequency, leftPulseWidth, rightPulseWidth, lAngle, rAngle):
        #s = ServoSG90.ServoSG90(23, 50, 2.5, 11.5, 0, 180)
        self.Frequency = frequency
        self.LeftPulseWidth= leftPulseWidth
        self.LeftAngle = lAngle

        self.RightPulseWidth = rightPulseWidth
        self.RightAngle = rAngle

        self.Running = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin,self.Frequency)
        ServoSG90.log.info("ServoSG90.init")

    def show(self):
        ServoSG90.log.info("ServoSG90.show")
    def ConfigServo(self, frequency, leftPulseWidth, rightPulseWidth):
        self.Frequency = frequency
        self.LeftPulseWidth = leftPulseWidth
        self.RightPulseWidth = rightPulseWidth
        ServoSG90.log.info("ServoSG90.ConfigServo {0} {1} {2}"
                           .format(frequency, leftPulseWidth, rightPulseWidth))
    def SetAngle(self, degree):
        ServoSG90.log.info("ServoSG90.SetAngle {0}".format(degree))
        m = (self.RightPulseWidth - self.LeftPulseWidth)/(self.RightAngle - self.LeftAngle)
        dc = m * degree + self.LeftPulseWidth
        self.SetPwm(dc)

    def SetPwm(self, dutyCycle):
        ServoSG90.log.info("ServoSG90.SetPwm {0}".format(dutyCycle))
        if(self.Running == False):
            self.pwm.start(dutyCycle)
            self.Running = True
        else:
            self.pwm.ChangeDutyCycle(dutyCycle)
        time.sleep(1)

    def Stop(self):
        self.Running = False
        self.pwm.stop()
        GPIO.cleanup()
