import logging
from multiprocessing import Queue
from threading import Thread
from time import sleep
from elMsg import elMsg
from MsgServo import *
from Drivers.ServoEnums import *
from Factory.ServoFactory import *
from Factory.CameraFactory import *
from MsgPic import *

class CmdQueue:

    log = logging.getLogger('SemBrain')
    
    def __init__(self):
        
        CmdQueue.log.info("CmdQueue created");        
        self.Running = False
        self.myq = Queue()  


    def start(self):
    
        CmdQueue.log.info('CmdQueue Starting')
    
        self.thread = Thread(target = self.queueProcessor, args = (10, ))
    
        self.thread.start()
    
    

        CmdQueue.log.info('ComdQueue Starting... complete')

    def addCommand(self, arg):
        self.myq.put(arg)    

    def stop(self):
        self.Running = False
        self.myq.put("e")
    
    def setCommInterface(self, comms):
        self.Comms = comms

    def queueProcessor(self, arg):
        CmdQueue.log.info("queueProcessor enter")   
        self.Running = True
        servoFactory = ServoFactory()
        cameraFactory = CameraFactory()
        while self.Running:
            CmdQueue.log.debug('q = {}!'.format(self.myq.qsize()))
            while not self.myq.empty():
                c = self.myq.get()
                if isinstance(c, elMsg):
                    CmdQueue.log.info('CMD: {0}'.format(c))
                elif isinstance(c, MsgElServo):
                    CmdQueue.log.info('CMD>Servo {0}'.format(c))
                    servoFactory.ExecuteCommand(c)
                elif isinstance(c, MsgPic):
                    CmdQueue.log.info('CMD>Pic {0}'.format(c))
                    cameraFactory.ExecuteCommand(c.PicFilename)
                    self.Comms.PushPic(c.PicFilename)
            
            sleep(1)     
    
        CmdQueue.log.info("queueProcessor exit")   
