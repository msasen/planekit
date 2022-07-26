class Wind:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.direction = None
            self.speed = None
            self.speed_z = None
        else:
            self.all = message
            self.direction = message.direction
            self.speed = message.speed
            self.speed_z = message.speed_z
