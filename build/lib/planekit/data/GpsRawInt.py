class GpsRawInt:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_usec = None
            self.fix_type = None
            self.lat = None
            self.lon = None
            self.alt = None
            self.eph = None
            self.epv = None
            self.vel = None
            self.cog = None
            self.satellites_visible = None
            self.alt_ellipsoid = None
            self.h_acc = None
            self.v_acc = None
            self.vel_acc = None
            self.hdg_acc = None
            self.yaw = None
        else:
            self.all = message
            self.time_usec = message.time_usec
            self.fix_type = message.fix_type
            self.lat = message.lat
            self.lon = message.lon
            self.alt = message.alt
            self.eph = message.eph
            self.epv = message.epv
            self.vel = message.vel
            self.cog = message.cog
            self.satellites_visible = message.satellites_visible
            self.alt_ellipsoid = message.alt_ellipsoid
            self.h_acc = message.h_acc
            self.v_acc = message.v_acc
            self.vel_acc = message.vel_acc
            self.hdg_acc = message.hdg_acc
            self.yaw = message.yaw
