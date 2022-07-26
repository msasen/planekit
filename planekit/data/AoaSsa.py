class AoaSsa:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_usec = None
            self.AOA = None
            self.SSA = None
        else:
            self.all = message
            self.time_usec = message.time_usec
            self.AOA = message.AOA
            self.SSA = message.SSA
