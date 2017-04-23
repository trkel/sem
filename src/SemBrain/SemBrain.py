import logging
import CmdQueue
import elMsg

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

    log.debug('starting cmdQueue')
    q = CmdQueue.CmdQueue()
    q.start()
    
    
    while True:
        c = input("Enter Command: ")
        if c == "e":
            log.debug("trying to quit")
            q.stop()
            break
        elif c=="m":
            log.debug("the m command was entered")
            cmsg = elMsg.elMsg('NewEl_M_Msg')
            q.addCommand(cmsg)
            # no break - exit the main while true server loop

   

if __name__ == '__main__':
    main()