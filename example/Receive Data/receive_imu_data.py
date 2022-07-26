import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
vehicle.wait_heartbeat()
print("connection is successful")
while True:
    imu_message = vehicle.imu_message()
    print(imu_message.xacc)
    print(imu_message.yacc)
    print(imu_message.zacc)
    print(imu_message.xmag)
    print(imu_message.ymag)
    print(imu_message.zmag)
    print(imu_message.xgyro)
    print(imu_message.ygyro)
    print(imu_message.zgyro)
