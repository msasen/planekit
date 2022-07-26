class ScaledImu3:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_boot_ms = None
            self.xacc = None
            self.yacc = None
            self.zacc = None
            self.xgyro = None
            self.ygyro = None
            self.zgyro = None
            self.xmag = None
            self.ymag = None
            self.zmag = None
            self.temperature = None
        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.xacc = message.xacc
            self.yacc = message.yacc
            self.zacc = message.zacc
            self.xgyro = message.xgyro
            self.ygyro = message.ygyro
            self.zgyro = message.zgyro
            self.xmag = message.xmag
            self.ymag = message.ymag
            self.zmag = message.zmag
            self.temperature = message.temperature
