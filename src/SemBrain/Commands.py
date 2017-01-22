class cmd(object):
    def __init__(self, name):
        self.name = name        
        
    
    def __str__(self):
        return 'cmd: {}'.format(self.name)

class AlarmOnCmd(cmd):
    def __init__(self, name, timeOn):
        cmd.__init__(self, name)
        self.timeOn = timeOn


    