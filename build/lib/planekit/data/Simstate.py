class Simstate:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.roll = None
            self.pitch = None
            self.yaw = None
            self.xacc = None
            self.yacc = None
            self.zacc = None
            self.xgyro = None
            self.ygyro = None
            self.zgyro = None
            self.lat = None
            self.lng = None
        else:
            self.all = message
            self.roll = message.roll
            self.pitch = message.pitch
            self.yaw = message.yaw
            self.xacc = message.xacc
            self.yacc = message.yacc
            self.zacc = message.zacc
            self.xgyro = message.xgyro
            self.ygyro = message.ygyro
            self.zgyro = message.zgyro
            self.lat = message.lat
            self.lng = message.lng
