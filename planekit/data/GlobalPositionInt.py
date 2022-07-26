class GlobalPositionInt:
    def __init__(self, message=None):
        if message is None:
            self.all = None
            self.time_boot_ms = None
            self.lat = None
            self.lon = None
            self.alt = None
            self.relative_alt = None
            self.vx = None
            self.vy = None
            self.vz = None
            self.hdg = None
        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.lat = message.lat
            self.lon = message.lon
            self.alt = message.alt
            self.relative_alt = message.relative_alt
            self.vx = message.vx
            self.vy = message.vy
            self.vz = message.vz
            self.hdg = message.hdg
