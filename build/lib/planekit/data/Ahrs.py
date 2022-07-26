class Ahrs:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.omegaIx = None
            self.omegaIy = None
            self.omegaIz = None
            self.accel_weight = None
            self.renorm_val = None
            self.error_rp = None
            self.error_yaw = None
        else:
            self.all = message
            self.omegaIx = message.omegaIx
            self.omegaIy = message.omegaIy
            self.omegaIz = message.omegaIz
            self.accel_weight = message.accel_weight
            self.renorm_val = message.renorm_val
            self.error_rp = message.error_rp
            self.error_yaw = message.error_yaw
