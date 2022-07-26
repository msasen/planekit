class EscTelemetry:
    def __init__(self, message=None):
        if message is None:
            self.all = None
            self.temperature = None
            self.voltage = None
            self.current = None
            self.totalcurrent = None
        else:
            self.all = message
            self.temperature = message.temperature
            self.voltage = message.voltage
            self.current = message.current
            self.totalcurrent = message.totalcurrent
