import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.wind.all)
    print(vehicle.message.wind.speed)
    print(vehicle.message.wind.speed_z)
    print(vehicle.message.wind.direction)