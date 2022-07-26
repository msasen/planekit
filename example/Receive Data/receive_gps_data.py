
import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
vehicle.wait_heartbeat()
print("connection is successful")
while True:
    gps_message = vehicle.gps_message()
    print("lat:" + str(gps_message.lat))
    print("lon:" + str(gps_message.lon))
    print("alt:" + str(gps_message.alt))
    print("vel:" + str(gps_message.vel))
    print("all gps fata " + str(gps_message.message))
    print("time usec " + str(gps_message.message.time_usec))
    print("fix type " + str(gps_message.message.fix_type))
    print("eph " + str(gps_message.message.eph))
    print("epv " + str(gps_message.message.epv))
    print("satellites_visible " + str(gps_message.message.satellites_visible))
    print("alt_ellipsoid " + str(gps_message.message.alt_ellipsoid))
    print("h_acc" + str(gps_message.message.h_acc))
    print("v_acc" + str(gps_message.message.v_acc))
    print("vel_acc" + str(gps_message.message.vel_acc))
    print("hdg_acc" + str(gps_message.message.hdg_acc))