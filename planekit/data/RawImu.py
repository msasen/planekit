class RawImu:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_usec = None
            self.xacc = None
            self.yacc = None
            self.zacc = None
            self.xgyro = None
            self.ygyro = None
            self.zgyro = None
            self.xmag = None
            self.ymag = None
            self.zmag = None
            self.id = None
            self.temperature = None
        else:
            self.all = message
            self.time_usec = message.time_usec
            self.xacc = message.xacc
            self.yacc = message.yacc
            self.zacc = message.zacc
            self.xgyro = message.xgyro
            self.ygyro = message.ygyro
            self.zgyro = message.zgyro
            self.xmag = message.xmag
            self.ymag = message.ymag
            self.zmag = message.zmag
            self.id = message.id
            self.temperature = message.temperature
