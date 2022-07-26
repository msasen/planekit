import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.ahrs.all)
    print(vehicle.message.ahrs.omegaIx)
    print(vehicle.message.ahrs.omegaIy)
    print(vehicle.message.ahrs.omegaIz)
    print(vehicle.message.ahrs.error_rp)
    print(vehicle.message.ahrs.accel_weight)
    print(vehicle.message.ahrs.error_yaw)
    print(vehicle.message.ahrs.renorm_val)