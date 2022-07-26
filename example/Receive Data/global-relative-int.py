import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

print("a11111111111111111111")
while True:
    print(vehicle.message.global_position)
    print(vehicle.message.global_position.alt)
    print(vehicle.message.global_position.all)
    print(vehicle.message.global_position.time_boot_ms)
    print(vehicle.message.global_position.lat)
    print(vehicle.message.global_position.lon)
    print(vehicle.message.global_position.hdg)
    print(vehicle.message.global_position.relative_alt)
    print(vehicle.message.global_position.vx)
    print(vehicle.message.global_position.vy)
    print(vehicle.message.global_position.vz)



