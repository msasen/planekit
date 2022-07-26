class Gps:
    def __init__(self, gps_message):
        self.message = gps_message
        self.timestamp = self.message._timestamp
        self.lat = self.message.lat
        self.lon = self.message.lon
        self.alt = self.message.alt
        self.vel = self.message.vel

    def retake_lat(self):
        self.lat = self.message.lat

    def get_lat(self):
        self.retake_lat()
        return self.lat

    def retake_vel(self):
        self.vel = self.message.vel

    def get_vel(self):
        self.retake_vel()
        return self.vel

    def retake_lon(self):
        self.lon = self.message.lon

    def get_lon(self):
        self.retake_lon()
        return self.lon

    def retake_alt(self):
        self.alt = self.message.alt

    def get_alt(self):
        self.retake_alt()
        return self.alt

    def retake_timestamp(self):
        self.timestamp = self.message.timestamp

    def get_timestamp(self):
        self.retake_timestamp()
        return self.timestamp
