class ServoOutputRaw:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_usec = None
            self.port = None
            self.servo1_raw = None
            self.servo2_raw = None
            self.servo3_raw = None
            self.servo4_raw = None
            self.servo5_raw = None
            self.servo6_raw = None
            self.servo7_raw = None
            self.servo8_raw = None
            self.servo9_raw = None
            self.servo10_raw = None
            self.servo11_raw = None
            self.servo12_raw = None
            self.servo13_raw = None
            self.servo14_raw = None
            self.servo15_raw = None
            self.servo16_raw = None
        else:
            self.all = message
            self.time_usec = message.time_usec
            self.port = message.port
            self.servo1_raw = message.servo1_raw
            self.servo2_raw = message.servo2_raw
            self.servo3_raw = message.servo3_raw
            self.servo4_raw = message.servo4_raw
            self.servo5_raw = message.servo5_raw
            self.servo6_raw = message.servo6_raw
            self.servo7_raw = message.servo7_raw
            self.servo8_raw = message.servo8_raw
            self.servo9_raw = message.servo9_raw
            self.servo10_raw = message.servo10_raw
            self.servo11_raw = message.servo11_raw
            self.servo12_raw = message.servo12_raw
            self.servo13_raw = message.servo13_raw
            self.servo14_raw = message.servo14_raw
            self.servo15_raw = message.servo15_raw
            self.servo16_raw = message.servo16_raw