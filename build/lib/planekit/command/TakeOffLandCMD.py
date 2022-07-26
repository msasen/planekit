import time

from pymavlink import mavutil
from pymavlink import mavwp


class TakeOffLandCMD:
    def __init__(self, connection_object, message_object):
        self.connection_object = connection_object
        self.message = message_object
        self.wp = mavwp.MAVWPLoader()

    def cmd_set_home(self, home_location, altitude):
        # print('--- ', self.connection_object.target_system, ',', self.connection_object.target_component)
        self.connection_object.mav.command_long_send(
            self.connection_object.target_system, self.connection_object.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_HOME,
            1,  # set position
            0,  # param1
            0,  # param2
            0,  # param3
            0,  # param4
            home_location[0],  # lat
            home_location[1],  # lon
            altitude)

    def upload_mission(self, lines):
        home_location = None
        home_altitude = None
        # print(lines)
        for i in range(0, 2):

            # print("*************************************")
            line = lines[i]
            mission_param = line.split('\t')
            # print(mission_param)
            ln_seq = int(mission_param[0])
            ln_current = int(mission_param[1])
            ln_frame = int(mission_param[2])
            ln_command = int(mission_param[3])
            ln_param1 = float(mission_param[4])
            ln_param2 = float(mission_param[5])
            ln_param3 = float(mission_param[6])
            ln_param4 = float(mission_param[7])
            ln_x = float(mission_param[8])
            ln_y = float(mission_param[9])
            ln_z = float(mission_param[10])
            ln_autocontinue = int(float(mission_param[11].strip()))
            if i == 1:
                home_location = (ln_x, ln_y)
                home_altitude = ln_z
            self.message.command_ack = None
            # print("msg"+str(self.message.command_ack))
            p = mavutil.mavlink.MAVLink_mission_item_message(self.connection_object.target_system,
                                                             self.connection_object.target_component, ln_seq,
                                                             ln_frame,
                                                             ln_command,
                                                             ln_current, ln_autocontinue, ln_param1, ln_param2,
                                                             ln_param3, ln_param4, ln_x, ln_y, ln_z)
            self.wp.add(p)

        self.cmd_set_home(home_location, home_altitude)
        print("1")
        while self.message.command_ack is  None:
            time.sleep(.1)
        str(self.message.command_ack)
        # print('Set home location: {0} {1}'.format(home_location[0], home_location[1]))
        time.sleep(1)
        print("al")
        self.message.mission_request = None
        # send waypoint to airframe
        self.connection_object.waypoint_clear_all_send()
        self.connection_object.waypoint_count_send(self.wp.count())

        for i in range(self.wp.count()):
            while self.message.mission_request is None:
                time.sleep(.1)
            str(self.message.mission_request)
            self.message.mission_request = None

    def takeoff_string(self, a):
        print("ssssssss")
        line = ["0	1	0	16	0	0	0	0	35.3633498	-149.1652373	585.040000	1",
                "1	0	3	22	40.00000000	0.00000000	0.00000000	0.00000000	-35.36574580	149.15974620	" + str(
                    a) + "	1"]

        # print(line)
        self.upload_mission(line)

    def lend_string(self, a):
        line = ["0	1	0	16	0	0	0	0	35.3633497	-149.1652372	585.039978	1",
                "1	0	3	21	0.00000000	0.00000000	0.00000000	1.00000000	-35.36329600	149.15901660	0.000000	1"]

        # print(line)
        self.upload_mission(line)
