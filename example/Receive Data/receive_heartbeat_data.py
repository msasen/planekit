
import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
vehicle.wait_heartbeat()
print("connection is successful")
while True:
    ahrs_message = vehicle.heartbeat_message().get_all_state()
    print(ahrs_message.type)
    print(ahrs_message.autopilot)
    print(ahrs_message.base_mode)
    print(ahrs_message.custom_mode)
    print(ahrs_message.system_status)
    print(ahrs_message.mavlink_version)