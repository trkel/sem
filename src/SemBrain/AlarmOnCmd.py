import mycmd

class AlarmOnCmd(mycmd):
    def __init__(self, name, timeOn):
        mycmd.__init__(self, name)
        self.timeOn = timeOn
    