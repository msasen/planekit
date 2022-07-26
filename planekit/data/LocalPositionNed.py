class LocalPositionNed:
    def __init__(self, message=None):
        if message is None:
            self.all = None
            self.time_boot_ms = None
            self.x = None
            self.y = None
            self.z = None
            self.vx = None
            self.vy = None
            self.vz = None

        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.x = message.z
            self.y = message.y
            self.z = message.z
            self.vx = message.vx
            self.vy = message.vy
            self.vz = message.vz
