import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.local_position_end.all)
    print(vehicle.message.local_position_end.x)
    print(vehicle.message.local_position_end.y)
    print(vehicle.message.local_position_end.z)
    print(vehicle.message.local_position_end.vx)
    print(vehicle.message.local_position_end.vy)
    print(vehicle.message.local_position_end.vz)
    print(vehicle.message.local_position_end.time_boot_ms)