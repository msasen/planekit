class Ahrs2:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.roll = None
            self.pitch = None
            self.yaw = None
            self.altitude = None
            self.lat = None
            self.lng = None
        else:
            self.all = message
            self.roll = message.roll
            self.pitch = message.pitch
            self.yaw = message.yaw
            self.altitude = message.altitude
            self.lat = message.lat
            self.lng = message.lng
