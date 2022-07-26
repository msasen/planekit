import sys

from pymavlink import mavutil
from planekit.exception.ConnectionIsNoneError import ConnectionIsNoneError


class Connection:
    def __init__(self):
        self.connection_object = None
        self.connection_string = None

    def get_connection(self):
        # Remove print
        # print(self.connection_string)
        a = ConnectionIsNoneError(self.connection_string)
        a.is_connection_none()
        # print(self.connection)
        if self.connection_object is None:
            sys.exit()
        return self.connection_object

    def connection(self, connection_string):
        self.connection_string = connection_string
        master = mavutil.mavlink_connection(connection_string)
        master.wait_heartbeat()
        self.connection_object = master
        return self.get_connection()
