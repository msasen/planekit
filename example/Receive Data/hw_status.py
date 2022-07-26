import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.hwstatus.all)
    print(vehicle.message.hwstatus.Vcc)
    print(vehicle.message.hwstatus.I2Cerr)