import logging
import CmdQueue

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
      c = raw_input("Enter Command: ")
      if c == "e":
        log.debug("trying to quit")
        q.stop()
        break
        
    
    

if __name__ == '__main__':
    main()