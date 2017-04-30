import logging



class ImageAcq(object):
    """description of class"""
    log = logging.getLogger('ImageAcq')

    def __init__(self):
        ImageAcq.log.info("ImageAcq __init__ entered")

    def takePicture(self, saveToPath):
        ImageAcq.log.info("take picutre")        
        #MyCam = VideoCapture(0)
        #s, img = MyCam.read()
        #if(s):
        #    ImageAcq.log.info("trying to save to: ", saveToPath)
        #    imwrite(saveToPath, img)
        #else:
        #    ImageAcq.log.warn("failed to acquire picture")

        #MyCam.release()
