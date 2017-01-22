import logging
import Queue
import cmd
from threading import Thread
from time import sleep

class CmdQueue:

    log = logging.getLogger('SemBrain')
    
    def __init__(self):
        
        CmdQueue.log.info("CmdQueue created");        
        self.Running = False
        self.q = Queue.Queue()   


    def start(self):
    
        CmdQueue.log.info('CmdQueue Starting')
    
        self.thread = Thread(target = self.queueProcessor, args = (10, ))
    
        self.thread.start()
    
    

        CmdQueue.log.info('ComdQueue Starting... complete')

    def addCommand(arg):
        self.q.put(arg)    

    def stop(self):
        self.Running = False
        self.q.put("e")
    

    def queueProcessor(self, arg):
        CmdQueue.log.info("queueProcessor enter")   
        self.Running = True
        while self.Running:
            CmdQueue.log.debug('q = {}!'.format(self.q.qsize()))
            while not self.q.empty():
                c = self.q.get()
                if isinstance(c, mycmd):
                    CmdQueue.log.info('CMD: {0}'.format(c))
                else:
                    CmdQueue.log.info('other: {0}'.format(c))
            
            sleep(1)     
    
        CmdQueue.log.info("queueProcessor exit")   
