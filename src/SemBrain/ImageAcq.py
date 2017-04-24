import logging
from cv2 import *


class ImageAcq(object):
    """description of class"""
    log = logging.getLogger('ImageAcq')

    def __init__(self):
        ImageAcq.log.info("ImageAcq __init__ entered")
        #self.MyCam = VideoCapture(0)

    def takePicture(self, saveToPath):
        
        MyCam = VideoCapture(0)
        s, img = MyCam.read()
        if(s):
            ImageAcq.log.info("trying to save to: ", saveToPath)
            imwrite(saveToPath, img)
        else:
            ImageAcq.log.warn("failed to acquire picture")

        MyCam.release()
