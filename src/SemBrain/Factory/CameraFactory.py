from enum import Enum
from subprocess import call
import logging
import time

class CameraFactory(object):
    """description of class"""
    log = logging.getLogger('SemBrain')

    def __init__(self):
        CameraFactory.log.info('CameraFactory.init')

    def ExecuteCommand(self, filename):
        CameraFactory.log.info('CameraFactory.takePicture')
        #call(["ls", "-l"])
