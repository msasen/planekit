class ScaledPressure:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.time_boot_ms = None
            self.press_abs = None
            self.press_diff = None
            self.temperature = None
            self.temperature_press_diff = None
        else:
            self.all = message
            self.time_boot_ms = message.time_boot_ms
            self.press_abs = message.press_abs
            self.press_diff = message.press_diff
            self.temperature = message.temperature
            self.temperature_press_diff = message.temperature_press_diff
