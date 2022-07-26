class Imu:
    def __init__(self, imu_message):
        self.message = imu_message
        # print(self.message)
        self.xacc = self.message.xacc
        self.yacc = self.message.yacc
        self.zacc = self.message.zacc
        self.xgyro = self.message.xgyro
        self.ygyro = self.message.ygyro
        self.zgyro = self.message.zgyro
        self.xmag = self.message.xmag
        self.ymag = self.message.ymag
        self.zmag = self.message.zmag

    def retake_xacc(self):
        self.xacc = self.message.xacc

    def get_xacc(self):
        self.retake_xacc()
        return self.xacc

    def retake_yacc(self):
        self.yacc = self.message.yacc

    def get_yacc(self):
        self.retake_yacc()
        return self.yacc

    def retake_zacc(self):
        self.zacc = self.message.zacc

    def get_zacc(self):
        self.retake_zacc()
        return self.zacc

    def retake_xgyro(self):
        self.xgyro = self.message.xgyro

    def get_xgyro(self):
        self.retake_xgyro()
        return self.xgyro

    def retake_ygyro(self):
        self.ygyro = self.message.ygyro

    def get_ygyro(self):
        self.retake_ygyro()
        return self.ygyro

    def retake_zgyro(self):
        self.zgyro = self.message.zgyro

    def get_zgyro(self):
        self.retake_zgyro()
        return self.zgyro

    def retake_xmag(self):
        self.xmag = self.message.xmag

    def get_xmag(self):
        self.retake_xmag()
        return self.xmag

    def retake_ymag(self):
        self.ymag = self.message.ymag

    def get_ymag(self):
        self.retake_ymag()
        return self.ymag

    def retake_zmag(self):
        self.zmag = self.message.zmag

    def get_zmag(self):
        self.retake_zmag()
        return self.zmag
