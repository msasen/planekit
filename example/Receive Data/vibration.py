import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.vibration.all)
    print(vehicle.message.vibration.vibration_x)
    print(vehicle.message.vibration.vibration_y)
    print(vehicle.message.vibration.vibration_z)
    print(vehicle.message.vibration.time_usec)
    print(vehicle.message.vibration.clipping_0)
    print(vehicle.message.vibration.clipping_1)
    print(vehicle.message.vibration.clipping_2)
