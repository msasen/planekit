class PowerStatus:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.Vcc = None
            self.Vservo = None
            self.flags = None
        else:
            self.all = message
            self.Vcc = message.Vcc
            self.Vservo = message.Vservo
            self.flags = message.flags
