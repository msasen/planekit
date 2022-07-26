class EkfStatusReport:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.flags = None
            self.velocity_variance = None
            self.pos_horiz_variance = None
            self.pos_vert_variance = None
            self.compass_variance = None
            self.terrain_alt_variance = None
            self.airspeed_variance = None
        else:
            self.all = message
            self.flags = message.flags
            self.velocity_variance = message.velocity_variance
            self.pos_horiz_variance = message.pos_horiz_variance
            self.pos_vert_variance = message.pos_vert_variance
            self.compass_variance = message.compass_variance
            self.terrain_alt_variance = message.terrain_alt_variance
            self.airspeed_variance = message.airspeed_variance
