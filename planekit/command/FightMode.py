import sys
import time

from planekit.mavlink.SendMessage import SendMessage
from planekit.mavlink.ReceiveData import ReceiveData

mode = ""


class FlightMode:
    def __init__(self, connection_object, message_object):
        self.connection_object = connection_object
        self.arm_status = None
        self.message = message_object

    def set_flight_mode(self, mode):
        # Choose a mode
        send_message = SendMessage(self.connection_object, self.message)
        if mode not in self.connection_object.mode_mapping():
            print('Unknown mode : {}'.format(mode))
            print('Try:', list(self.connection_object.mode_mapping().keys()))
            sys.exit(1)

        self.message.command_ack = None
        mode_id = self.connection_object.mode_mapping()[mode]
        # Set new mode
        # self.connection_object.mav.command_long_send(
        #    self.connection_object.target_system, self.connection_object.target_component,
        #    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
        #    0, mode_id, 0, 0, 0, 0, 0) or:
        # self.connection_object.set_mode(mode_id) or:
        self.connection_object.mav.set_mode_send(
            self.connection_object.target_system,
            send_message.mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)
        # Wait for ACK command
        # Would be good to add mechanism to avoid endlessly blocking
        # if the autopilot sends a NACK or never receives the message
        while self.message.command_ack is None:
            time.sleep(0.1)
        print(self.message.command_ack)

    def get_flight_mode(self):
        global mode
        all_mode = ['MANUAL', 'CIRCLE', 'STABILIZE', 'TRAINING', 'ACRO', 'FBWA', 'FBWB', 'CRUISE', 'AUTOTUNE', "AUTO",
                    'AUTO',
                    'RTL', 'LOITER', 'TAKEOFF', 'AVOID_ADSB', 'GUIDED', 'INITIALISING', 'QSTABILIZE', 'QHOVER',
                    'QLOITER', 'QLAND', 'QRTL', 'QAUTOTUNE', 'QACRO', 'THERMAL', 'LOITERALTQLAND']
        if self.message.heartbeat_message.all.type == 1:
            mode = all_mode[self.message.heartbeat_message.all.custom_mode]
        return mode
