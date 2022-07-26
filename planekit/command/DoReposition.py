import time

from pymavlink import mavutil

mode = ""


class DoReposition:
    def __init__(self, connection_object, message_object):
        self.connection_object = connection_object
        self.message = message_object

    def go_waypoint(self, lat, lon, alt):
        self.message.command_ack = None
        self.connection_object.mav.command_int_send(
            0,
            0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
            mavutil.mavlink.MAV_CMD_DO_REPOSITION,
            0,
            0,
            -1,
            0,
            0,
            0,
            int(lat * 1e7),
            int(lon * 1e7),
            alt,
        )
        while self.message.command_ack is None:
            time.sleep(0.1)
        print(self.message.command_ack)
