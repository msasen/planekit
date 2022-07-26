import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
vehicle.wait_heartbeat()
print("connection is successful")

while True:
    print("Lat: %s" % vehicle.lat())
    print("Lon: %s" % vehicle.lon())
    print("alt: %s" % vehicle.alt())
    print("ground speed: %s" % vehicle.ground_speed())
    print("arm status: %s" % vehicle.arm_status())
    print("mode: %s" % vehicle.mode())
    time.sleep(1)