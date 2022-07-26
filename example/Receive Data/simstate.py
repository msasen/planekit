import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.simstate.all)
    print(vehicle.message.simstate.lat)
    print(vehicle.message.simstate.yaw)
    print(vehicle.message.simstate.pitch)
    print(vehicle.message.simstate.lng)
    print(vehicle.message.simstate.xgyro)
    print(vehicle.message.simstate.xacc)
    print(vehicle.message.simstate.yacc)
    print(vehicle.message.simstate.zacc)
    print(vehicle.message.simstate.ygyro)
    print(vehicle.message.simstate.zgyro)
    print(vehicle.message.simstate.roll)