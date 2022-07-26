import time
from planekit.Calculator import Calculator
from planekit.command.DoReposition import DoReposition
from planekit.command.FightMode import FlightMode
from planekit.command.SetArm import SetArm
from planekit.command.TakeOffLandCMD import TakeOffLandCMD
from planekit.data.Imu import Imu
from planekit.mavlink.Connection import Connection as MavLinkConnection
from planekit.mavlink.ReceiveData import ReceiveData
from planekit.mavlink.SendMessage import SendMessage


class Connection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.mavlink = MavLinkConnection()
        self.connection_object = self.mavlink.connection(connection_string)
        self.message = ReceiveData(self.connection_object)
        self.message.start_data_thread()

    def arm(self):
        set_arm = SetArm(self.connection_object, self.message)
        set_arm.arm()

    def disarm(self):
        set_arm = SetArm(self.connection_object, self.message)
        set_arm.disarm()

    """
    def takeoff(self, alt):
        takeoff = TakeOffLandCMD(self.connection_object, self.message)
        takeoff.takeoff_string(alt)
        self.set_flight_mode("AUTO")
        while self.mode() != "AUTO":
            print("mode ayarlanıyor")
            self.set_flight_mode("AUTO")
            time.sleep(1)
    """

    def set_flight_mode(self, mode):
        set_flight_modes = FlightMode(self.connection_object, self.message)
        set_flight_modes.set_flight_mode(mode)

    def mode(self):
        return FlightMode(self.connection_object, self.message).get_flight_mode()

    def set_rc_channel_pwm(self, channel_id, pwm=1500):
        """ Set RC channel pwm value
        Args:
            channel_id (TYPE): Channel ID
            pwm (int, optional): Channel pwm value 1100-1900
        """
        if channel_id < 1 or channel_id > 18:
            print("Channel does not exist.")
            return

        rc_channel_values = [65535 for _ in range(18)]
        rc_channel_values[channel_id - 1] = pwm
        self.connection_object.mav.rc_channels_override_send(
            self.connection_object.target_system,  # target_system
            self.connection_object.target_component,  # target_component
            *rc_channel_values)  # RC channel list, in microseconds.


"""


class Connection:
    def __init__(self, connection_string):
        self.connection_string = connection_string

        self.mavlink = MavLinkConnection()
        self.connection_object = self.mavlink.connection(connection_string)

        self.message = ReceiveData(self.connection_object)
        self.message.start_data_thread()

    def wait_heartbeat(self):
        m = SendMessage(self.connection_object, self.message)
        m.wait_heartbeat()

    # Test remove prod.
    def get_connection(self):
        self.mavlink.get_connection()

    def messages(self):
        return self.message

    def imu_message(self):
        return ReceiveData(self.connection_object).select_imu_message()

    def gps_message(self):
        return ReceiveData(self.connection_object).select_gps_message()

    def heartbeat_message(self):
        return ReceiveData(self.connection_object).select_heartbeat_message()

    def ahrs_message(self):
        return ReceiveData(self.connection_object).select_ahrs_message()

    def lat(self):
        return ReceiveData(self.connection_object).select_gps_message().lat / 10000000

    def lon(self):
        return ReceiveData(self.connection_object).select_gps_message().lon / 10000000

    def alt(self):
        return ReceiveData(self.connection_object).alt()

    def ground_speed(self):
        return ReceiveData(self.connection_object).ground_speed_message() / 100

    def arm_status(self):
        return ReceiveData(self.connection_object).arm_status()

    def mode(self):
        return FlightMode(self.connection_object,self.message).get_flight_mode()

    def arm(self):
        set_arm = SetArm(self.connection_object, self.message)
        set_arm.arm()

    def disarm(self):
        set_arm = SetArm(self.connection_object, self.message)
        set_arm.disarm()

    def set_flight_mode(self, mode):
        set_flight_modes = FlightMode(self.connection_object, self.message)
        set_flight_modes.set_flight_mode(mode)

    def takeoff_and_arm(self, alt):
        takeoff = TakeOffLandCMD(self.connection_object, self.message)
        takeoff.takeoff_string(alt)
        self.arm()
        self.set_flight_mode("AUTO")
        while self.mode() != "AUTO":
            # print(self.mode())
            self.set_flight_mode("AUTO")
            time.sleep(10)

    def land_and_disarm(self):
        while self.arm_status() is True:
            land = TakeOffLandCMD(self.connection_object)
            land.lend_string(12)
            # print(self.mode())
            print("landing")
            self.set_flight_mode("AUTO")
            time.sleep(10)

    def go_to(self, lat, lon, alt, sleep=False):
        reposition = DoReposition(self.connection_object,self.message)
        reposition.go_waypoint(lat, lon, alt)
        while sleep:
            a = self.gps_message()
            print(Calculator.haversine(lat, lon, a.lat / 10000000, a.lon / 10000000))
            if Calculator.haversine(lat, lon, a.lat / 10000000, a.lon / 10000000) < 0.200:
                break

    def a(self):
        return self.connection_object

"""
