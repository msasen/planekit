import time


from pymavlink import mavutil


class SendMessage:
    def __init__(self, connection_object, message_object):
        self.connection_object = connection_object
        self.mavutil = mavutil
        self.message = message_object

    def wait_heartbeat(self):
        self.connection_object.wait_heartbeat()

    def send_cmd(self, command, p1, p2, p3, p4, p5, p6, p7, target_sysid=None, target_compid=None):
        """Send a MAVLink command long."""
        self.connection_object.mav.command_long_send(target_sysid, target_compid, command, 1,  # confirmation
                                                     p1, p2, p3, p4, p5, p6, p7)

    def run_cmd(self, command, p1, p2, p3, p4, p5, p6, p7, want_result=mavutil.mavlink.MAV_RESULT_ACCEPTED):
        target_sysid = self.connection_object.target_system
        target_compid = self.connection_object.target_component
        timeout = 10
        quiet = False
        self.send_cmd(command, p1, p2, p3, p4, p5, p6, p7, target_sysid=target_sysid, target_compid=target_compid)
        self.run_cmd_get_ack(command, want_result, timeout, quiet=quiet)

    def run_cmd_get_ack(self, command, want_result, timeout, quiet=False):
        # tstart = get_sim_time_cached()
        self.message.command_ack = None
        while True:
            # delta_time = get_sim_time_cached() - tstart
            # if delta_time > timeout:
            #    raise AutoTestTimeoutException("Did not get good COMMAND_ACK within %fs" % timeout)
            #    print('ERROR', "Did not get good COMMAND_ACK within %fs" % timeout)
            while self.message.command_ack is None:
                time.sleep(0.1)
            m = self.message.command_ack

            if m is None:
                continue
            if not quiet:
                pass
            if m.command == command:
                break
