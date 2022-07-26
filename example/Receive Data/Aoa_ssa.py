import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

print("a11111111111111111111")
while True:
    print(vehicle.message.aoa_ssa.all)
    print(vehicle.message.aoa_ssa.AOA)
    print(vehicle.message.aoa_ssa.time_usec)
    print(vehicle.message.aoa_ssa.SSA)