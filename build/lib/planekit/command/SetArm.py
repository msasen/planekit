import time

import planekit
from planekit.mavlink.SendMessage import SendMessage


class SetArm:
    def __init__(self, connection_object, message_object):
        self.connection_object = connection_object
        self.arm_status = None
        self.message = message_object

    def arm(self):
        while self.connection_object.motors_armed() != 128:
            self.arm_status = planekit.ReceiveData(self.connection_object).arm_status()
            send_message = SendMessage(self.connection_object, self.message)
            send_message.run_cmd(
                send_message.mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,  # command
                1,  # param1 (1 to indicate arm)
                1,  # param2  (all other params meaningless)
                0,  # param3
                0,  # param4
                0,  # param5
                0,  # param6
                0  # param7
            )
            time.sleep(1)

    def disarm(self):
        while self.connection_object.motors_armed() != 0:
            send_message = SendMessage(self.connection_object, self.message)
            send_message.run_cmd(
                send_message.mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,  # command
                0,  # param1 (1 to indicate arm)
                1,  # param2  (all other params meaningless)
                0,  # param3
                0,  # param4
                0,  # param5
                0,  # param6
                0  # param7
            )
