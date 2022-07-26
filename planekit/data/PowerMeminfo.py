class PowerMeminfo:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.brkval = None
            self.freemem = None
            self.freemem32 = None
        else:
            self.all = message
            self.brkval = message.brkval
            self.freemem = message.freemem
            self.freemem32 = message.freemem32
