import sys
import logging
import CmdQueue
import elMsg
from MsgServo import *
import os
import time
import io
import SlackComms
import ImageAcq
import uuid
from MsgPic import *

#sudo apt-get install libopencv-dev python-opencv
#import cv2
#from cv2 import *

log = logging.getLogger('SemBrain')


def initLogger():
    # create logger
    
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    
    log.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    log.addHandler(ch)
    
    log.debug('debug message')
    log.info('info message')
    log.warn('warn message')
    log.error('error message')
    log.critical('critical message')
    

def main():
    initLogger()
    log.debug("settings init")

    cam = ImageAcq.ImageAcq()
    filename = str(uuid.uuid4())[:8] + ".png"
    cam.takePicture(filename)


    log.debug('starting cmdQueue')
    q = CmdQueue.CmdQueue()
    q.start()

    sl = SlackComms.SlackComms(q)
    sl.start()
    
    q.setCommInterface(sl)


    while True:
        print ("Enter Command: ")
        # stdin.readline is used rather than input() because it'll be run over ssh. 
        # and there is funky stuff with buffering lines over ssh
        c = sys.stdin.readline()
        c = c.strip()

        # where the command will get parsed at the top level
        if c == "e":
            log.debug("trying to quit")
            q.stop()
            break
        elif c=="m":
            log.debug("the m command was entered")
            cmsg = MsgPic("custom name", "take pic", "sammypic.png")
            q.addCommand(cmsg)
            # no break - exit the main while true server loop
        elif c=="n":
            cmsg = MsgElServo("new servo", ServoAction.Open, "E1")
            q.addCommand(cmsg)
   

if __name__ == '__main__':
    main()
