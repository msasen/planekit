import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.ahrs2.all)
    print(vehicle.message.ahrs2.roll)
    print(vehicle.message.ahrs2.pitch)
    print(vehicle.message.ahrs2.yaw)
    print(vehicle.message.ahrs2.altitude)
    print(vehicle.message.ahrs2.lat)
    print(vehicle.message.ahrs2.lng)