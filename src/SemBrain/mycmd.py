class mycmd(object):
    def __init__(self, name):
        self.name = name        
        return super(cmd, self).__init__(name)
    
    def __str__(self):
        return super(cmd, self).__str__()