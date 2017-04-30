from abc import ABCMeta, abstractmethod
import logging

class IServo:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"
    @abstractmethod
    def show(self): raise NotImplementedError
    @abstractmethod
    def ConfigServo(self, frequency, leftPulseWidth, rightPulseWidth): raise NotImplementedError
    @abstractmethod
    def SetAngle(self, degree): raise NotImplementedError

class BaseServo(IServo):
    """Base Servo Class"""
    log = logging.getLogger('BaseServo')
    def __init__(self):
        BaseServo.log.info("BaseServo.init")
    def show(self):
        BaseServo.log.info("BaseServo.show")
    def ConfigServo(self, frequency, leftPulseWidth, rightPulseWidth):
        BaseServo.log.info("BaseServo.ConfigServo {0} {1} {2}"
                           .format(frequency, leftPulseWidth, rightPulseWidth))
    def SetAngle(self, degree):
        BaseServo.log.info("BaseServo.SetAngle {0}".format(degree))
