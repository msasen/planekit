class Heartbeat:
    def __init__(self, gps_message):
        self.message = gps_message
        self.type = self.message.type
        self.autopilot = self.message.autopilot
        self.base_mode = self.message.base_mode
        self.custom_mode = self.message.custom_mode
        self.system_status = self.message.system_status
        self.mavlink_version = self.message.mavlink_version
        self.arm = None

    def get_all_state(self):
        return self.message

    def get_custom_mode(self):
        return self.custom_mode

    def get_autopilot(self):
        return self.autopilot

    def get_base_mode(self):
        return self.base_mode

    def get_system_status(self):
        return self.system_status

    def get_mavlink_version(self):
        return self.mavlink_version
    """
    def is_arm(self):
        En:
            This function controls the arm status
            if system_status is equals 3 it means disarm,
            if system_status is equals 4 it means arm

            :return False if disarm
            :return True if arm
            :return -1(int) if another thing

        Tr:
            Bu fonksiyon arm drumunu kontrol eder
            system_status 3'e eşitse disarm,
            system_status 4'e  eşitse arm
            durumundadır.
        if self.system_status == 4:
            self.arm = True
            return self.arm
        if self.system_status == 3:
            self.arm = False
            return self.arm
        return -1
    """
