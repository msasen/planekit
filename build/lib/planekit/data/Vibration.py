class Vibration:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_usec = None
            self.vibration_x = None
            self.vibration_y = None
            self.vibration_z = None
            self.clipping_0 = None
            self.clipping_1 = None
            self.clipping_2 = None
        else:
            self.all = message
            self.time_usec = message.time_usec
            self.vibration_x = message.vibration_x
            self.vibration_y = message.vibration_y
            self.vibration_z = message.vibration_z
            self.clipping_0 = message.clipping_0
            self.clipping_1 = message.clipping_1
            self.clipping_2 = message.clipping_2
