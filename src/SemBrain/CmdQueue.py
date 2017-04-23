import logging
from multiprocessing import Queue
from threading import Thread
from time import sleep
from elMsg import elMsg

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
    

    def queueProcessor(self, arg):
        CmdQueue.log.info("queueProcessor enter")   
        self.Running = True
        while self.Running:
            CmdQueue.log.debug('q = {}!'.format(self.myq.qsize()))
            while not self.myq.empty():
                c = self.myq.get()
                if isinstance(c, elMsg):
                    CmdQueue.log.info('CMD: {0}'.format(c))
                else:
                    CmdQueue.log.info('other: {0}'.format(c))
            
            sleep(1)     
    
        CmdQueue.log.info("queueProcessor exit")   
