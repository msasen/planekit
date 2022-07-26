import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")

while True:
    print(vehicle.message.position_target_global_int.all)
    print(vehicle.message.position_target_global_int.yaw)
    print(vehicle.message.position_target_global_int.alt)
    print(vehicle.message.position_target_global_int.yaw_rate)
    print(vehicle.message.position_target_global_int.time_boot_ms)
    print(vehicle.message.position_target_global_int.vz)
    print(vehicle.message.position_target_global_int.vy)
    print(vehicle.message.position_target_global_int.vx)
    print(vehicle.message.position_target_global_int.afx)
    print(vehicle.message.position_target_global_int.afy)
    print(vehicle.message.position_target_global_int.afz)
    print(vehicle.message.position_target_global_int.coordinate_frame)
    print(vehicle.message.position_target_global_int.type_mask)