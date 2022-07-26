class MissionCurrent:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.seq = None
        else:
            self.all = message
            self.seq = message.seq
