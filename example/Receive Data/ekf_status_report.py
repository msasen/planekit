import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.ekf_status_report.all)
    print(vehicle.message.ekf_status_report.flags)
    print(vehicle.message.ekf_status_report.pos_horiz_variance)
    print(vehicle.message.ekf_status_report.pos_vert_variance)
    print(vehicle.message.ekf_status_report.airspeed_variance)
    print(vehicle.message.ekf_status_report.compass_variance)
    print(vehicle.message.ekf_status_report.terrain_alt_variance)
    print(vehicle.message.ekf_status_report.velocity_variance)