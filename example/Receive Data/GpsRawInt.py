import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

print("a11111111111111111111")
while True:
    print(vehicle.message.attitude.time_boot_ms)
    print(vehicle.message.attitude.yaw)
    print(vehicle.message.attitude.roll)
    print(vehicle.message.attitude.pitch)
    print(vehicle.message.attitude.rollspeed)
    print(vehicle.message.attitude.pitchspeed)
    print(vehicle.message.attitude.yawspeed)





