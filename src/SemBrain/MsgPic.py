class MsgPic(object):
    """description of class"""
    
    def __init__(self, name, command, picFilename):
        self.Name = name
        self.Command = command
        self.PicFilename = picFilename

    def __str__(self):
        return "Cmd: {0} {1}".format(self.Command, self.PicFilename)


