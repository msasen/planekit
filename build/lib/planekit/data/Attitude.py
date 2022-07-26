class Attitude:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_boot_ms = None
            self.roll = None
            self.pitch = None
            self.yaw = None
            self.rollspeed = None
            self.pitchspeed = None
            self.yawspeed = None
        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.roll = message.roll
            self.pitch = message.pitch
            self.yaw = message.yaw
            self.rollspeed = message.rollspeed
            self.pitchspeed = message.pitchspeed
            self.yawspeed = message.yawspeed
