class PositionTargetGlobalInt:
    def __init__(self, message=None):
        if message is None:
            self.all = None
            self.time_boot_ms = None
            self.coordinate_frame = None
            self.type_mask = None
            self.lon_int = None
            self.alt = None
            self.vx = None
            self.vy = None
            self.vz = None
            self.afx = None
            self.afy = None
            self.afz = None
            self.yaw = None
            self.yaw_rate = None
        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.coordinate_frame = message.coordinate_frame
            self.type_mask = message.type_mask
            self.lon_int = message.lon_int
            self.alt = message.alt
            self.vx = message.vx
            self.vy = message.vy
            self.vz = message.vz
            self.afx = message.afx
            self.afy = message.afy
            self.afz = message.afz
            self.yaw = message.yaw
            self.yaw_rate = message.yaw_rate
