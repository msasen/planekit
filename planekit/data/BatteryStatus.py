class BatteryStatus:
    def __init__(self, message=None):
        if message is None:
            self.all = None
            self.temperature = None
            self.voltages = None
            self.current_battery = None
            self.current_consumed = None
            self.energy_consumed = None
            self.battery_remaining = None
            self.time_remaining = None
            self.charge_state = None
            self.voltages_ext = None
            self.mode = None
            self.fault_bitmask = None
        else:
            self.all = message
            self.temperature = message.temperature
            self.voltages = message.voltages
            self.current_battery = message.current_battery
            self.current_consumed = message.current_consumed
            self.energy_consumed = message.energy_consumed
            self.battery_remaining = message.battery_remaining
            self.time_remaining = message.time_remaining
            self.charge_state = message.charge_state
            self.voltages_ext = message.voltages_ext
            self.mode = message.mode
            self.fault_bitmask = message.fault_bitmask
