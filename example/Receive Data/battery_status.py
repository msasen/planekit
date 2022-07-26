import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.battery_status.all)
    print(vehicle.message.battery_status.temperature)
    print(vehicle.message.battery_status.charge_state)
    print(vehicle.message.battery_status.fault_bitmask)
    print(vehicle.message.battery_status.mode)
    print(vehicle.message.battery_status.battery_remaining)
    print(vehicle.message.battery_status.current_consumed)
    print(vehicle.message.battery_status.energy_consumed)
    print(vehicle.message.battery_status.time_remaining)
    print(vehicle.message.battery_status.voltages)
    print(vehicle.message.battery_status.voltages_ext)
