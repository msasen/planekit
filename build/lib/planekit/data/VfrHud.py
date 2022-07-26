class VfrHud:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.airspeed = None
            self.groundspeed = None
            self.heading = None
            self.throttle = None
            self.alt = None
            self.climb = None
        else:
            self.all = message
            self.airspeed = message.airspeed
            self.groundspeed = message.groundspeed
            self.heading = message.heading
            self.throttle = message.throttle
            self.alt = message.alt
            self.climb = message.climb
