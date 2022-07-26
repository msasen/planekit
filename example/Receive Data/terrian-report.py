import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.terrain_report.all)
    print(vehicle.message.terrain_report.spacing)
    print(vehicle.message.terrain_report.lon)
    print(vehicle.message.terrain_report.lat)
    print(vehicle.message.terrain_report.terrain_height)
    print(vehicle.message.terrain_report.current_height)
    print(vehicle.message.terrain_report.loaded)
    print(vehicle.message.terrain_report.pending)