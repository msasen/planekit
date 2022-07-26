class HwStatus:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.Vcc = None
            self.I2Cerr = None
        else:
            self.all = message
            self.Vcc = message.Vcc
            self.I2Cerr = message.I2Cerr