from threading import Thread

from planekit.data.Ahrs import Ahrs
from planekit.data.Gps import Gps
from planekit.data.Heartbeat import Heartbeat
from planekit.data.Imu import Imu
from planekit.data.Attitude import Attitude
from planekit.data.GlobalPositionInt import GlobalPositionInt
from planekit.data.EscTelemetry import EscTelemetry
from planekit.data.AoaSsa import AoaSsa
from planekit.data.BatteryStatus import BatteryStatus
from planekit.data.PositionTargetGlobalInt import PositionTargetGlobalInt
from planekit.data.Vibration import Vibration
from planekit.data.LocalPositionNed import LocalPositionNed
from planekit.data.EkfStatusReport import EkfStatusReport
from planekit.data.TerrainReport import TerrainReport
from planekit.data.Wind import Wind
from planekit.data.HwStatus import HwStatus
from planekit.data.Ahrs2 import Ahrs2
from planekit.data.Simstate import Simstate
from planekit.data.Ahrs import Ahrs
from planekit.data.GpsRawInt import GpsRawInt
from planekit.data.ScaledPressure2 import ScaledPressure2
from planekit.data.ScaledPressure import ScaledPressure
from planekit.data.ScaledImu3 import ScaledImu3
from planekit.data.ScaledImu2 import ScaledImu2
from planekit.data.RawImu import RawImu
from planekit.data.RcChannels import RcChannels
from planekit.data.ServoOutputRaw import ServoOutputRaw
from planekit.data.MissionCurrent import MissionCurrent
from planekit.data.VfrHud import VfrHud
from planekit.data.PowerMeminfo import PowerMeminfo
from planekit.data.PowerStatus import PowerStatus


# noinspection PyAttributeOutsideInit
class ReceiveData:
    """
    En:
        This class parses mavtcp messages by type and sends them to the corresponding classes.
        :arg connection_object
            Gets the object instance pymavlink.mavutil.mavtcp
    Tr:
        Bu sınıf, mavtcp mesajlarını get_type ile ayrıştırır ve bunları ilgili sınıflara gönderir.
        :arg connection_object
            pymavlink.mavutil.mavtcp den türetilmiş objeyi alır
    """

    def __init__(self, connection_object):
        self.connection_object = connection_object
        self.message_object = None

        self.attitude = Attitude()
        self.global_position = GlobalPositionInt()
        self.esc_telemetry = EscTelemetry()
        self.aoa_ssa = AoaSsa()
        self.battery_status = BatteryStatus()
        self.position_target_global_int = PositionTargetGlobalInt()
        self.vibration = Vibration()
        self.local_position_end = LocalPositionNed()
        self.ekf_status_report = EkfStatusReport()
        self.terrain_report = TerrainReport()
        self.wind = Wind()
        self.hwstatus = HwStatus()
        self.ahrs2 = Ahrs2()
        self.simstate = Simstate()
        self.ahrs = Ahrs()
        # Aşağıdakiler için örnekler yazılacak
        self.gps_raw_int = GpsRawInt()
        self.scaled_pressure2 = ScaledPressure2()
        self.scaled_pressure = ScaledPressure()
        self.scaled_imu3 = ScaledImu3()
        self.scaled_imu2 = ScaledImu2()
        self.raw_imu = RawImu()
        self.rc_channels = RcChannels()
        self.servo_output_raw = ServoOutputRaw()
        self.mission_current = MissionCurrent()
        self.vfr_hud = VfrHud()
        self.power_meminfo = PowerMeminfo()
        self.power_status = PowerStatus()
        self.heartbeat_message = Heartbeat()
        self.command_ack = None
        self.mission_request = None
        '''
        ! None dönenler
        self.mav_controller_output = None
        self.param_value = None
        self.airspeed_autocal = None
        self.system_time = None
        '''
        self.imu_message = None
        self.gps_message = None
        # self.heartbeat_message = None
        self.ahrs_message = None

    def get_message(self):
        while True:
            self.message_object = self.connection_object.recv_match()
            if self.message_object is not None and self.message_object.get_type() == 'RAW_IMU':
                self.raw_imu = RawImu(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'COMMAND_ACK':
                self.command_ack = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'MISSION_REQUEST':
                self.mission_request = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'ATTITUDE':
                self.attitude = Attitude(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'GLOBAL_POSITION_INT':
                self.global_position = GlobalPositionInt(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SYS_STATUS':
                self.sys_status = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'POWER_STATUS':
                self.power_status = PowerStatus(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'MEMINFO':
                self.power_meminfo = PowerMeminfo(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'NAV_CONTROLLER_OUTPUT':
                self.mav_controller_output = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'MISSION_CURRENT':
                self.mission_current = MissionCurrent(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'VFR_HUD':
                self.vfr_hud = VfrHud(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SERVO_OUTPUT_RAW':
                self.servo_output_raw = ServoOutputRaw(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'RC_CHANNELS':
                self.rc_channels = RcChannels(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SCALED_IMU2':
                self.scaled_imu2 = ScaledImu2(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SCALED_IMU3':
                self.scaled_imu3 = ScaledImu3(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SCALED_PRESSURE':
                self.scaled_pressure = ScaledPressure(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SCALED_PRESSURE2':
                self.scaled_pressure2 = ScaledPressure2(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'GPS_RAW_INT':
                self.gps_raw_int = GpsRawInt(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SYSTEM_TIME':
                self.system_time = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'AHRS':
                self.ahrs = Ahrs(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'SIMSTATE':
                self.simstate = Simstate(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'AHRS2':
                self.ahrs2 = Ahrs2(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'HWSTATUS':
                self.hwstatus = HwStatus(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'WIND':
                self.wind = Wind(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'TERRAIN_REPORT':
                self.terrain_report = TerrainReport(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'EKF_STATUS_REPORT':
                self.ekf_status_report = EkfStatusReport(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'LOCAL_POSITION_NED':
                self.local_position_end = LocalPositionNed(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'VIBRATION':
                self.vibration = Vibration(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'POSITION_TARGET_GLOBAL_INT':
                self.position_target_global_int = PositionTargetGlobalInt(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'BATTERY_STATUS':
                self.battery_status = BatteryStatus(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'AOA_SSA':
                self.aoa_ssa = AoaSsa(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'ESC_TELEMETRY_1_TO_4':
                self.esc_telemetry = EscTelemetry(self.message_object)

            if self.message_object is not None and self.message_object.get_type() == 'AIRSPEED_AUTOCAL':
                self.airspeed_autocal = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'PARAM_VALUE':
                self.param_value = self.message_object

            if self.message_object is not None and self.message_object.get_type() == 'HEARTBEAT':
                self.heartbeat_message = Heartbeat(self.message_object)

    def start_data_thread(self):
        t = Thread(target=self.get_message)
        t.start()
        t = Thread()
        t.start()

    """
    Oldest
    """

    def get_message_object(self):
        """
        en:
            :return:
            self.message_object : Return messages received with recv_match.
        tr:
            :return:
                self.message_object : recv_match ile alınan mesajları dönderir.
        """

        self.message_object = self.connection_object.recv_match()
        return self.message_object

    def select_imu_message(self):
        """
        En:
            This func. selects imu messages received from self.get_message_object.
        Tr:
            Bu func. self.get_message_object'den alınan imu mesajlarını seçer.
        """

        return self.raw_imu

    def select_gps_message(self):
        """
            En:
                This func. selects gps messages received from self.get_message_object.
            Tr:
                Bu func. self.get_message_object'den alınan gps mesajlarını seçer.
        """
        return self.gps_raw_int

    def select_heartbeat_message(self):
        print("error")
        return self.heartbeat_message

    def select_ahrs_message(self):
        return self.ahrs2

    """
    def arm_status(self):
            En:
                Heartbeat(self.heartbeat_message).arm can have 3 values.
                These are True(if arm) False(if disarm) and -1(another thing).
            Tr:
                Heartbeat(self.heartbeat_message).arm 3 değere sahip olabilir.
                Bunlar True(if arm) False(if disarm) ve -1(another thing) olabilir.

        while True:
            self.heartbeat_message = planekit.ReceiveData(self.connection_object).get_message_object()
            if self.heartbeat_message is not None and self.heartbeat_message.get_type() == 'HEARTBEAT':
                heartbeat_message = Heartbeat(self.heartbeat_message)
                if heartbeat_message.is_arm() != -1:
                    return heartbeat_message.is_arm()
    """

    def arm_status(self):
        if self.connection_object.motors_armed() == 128:
            print("disarmed")
            return True
        if self.connection_object.motors_armed() == 0:
            print("armed")
            return False

    def ground_speed_message(self):
        """
            En:
                :return:
                    Return the vel parameter from messages with type GPS_RAW_INT
            Tr:
                :return:
                    GPS_RAW_INT tipine sahip mesajlardan vel parametresini dönderir
        """

        return self.gps_raw_int.vel

    def alt(self, relative=True, timeout=30):
        return self.global_position.relative_alt / 1000
