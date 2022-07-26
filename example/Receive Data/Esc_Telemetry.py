import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

print("a11111111111111111111")
while True:
    print(vehicle.message.esc_telemetry.all)
    print(vehicle.message.esc_telemetry.voltage)
    print(vehicle.message.esc_telemetry.current)
    print(vehicle.message.esc_telemetry.temperature)
    print(vehicle.message.esc_telemetry.totalcurrent)
