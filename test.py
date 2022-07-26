import time
import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
print("connection is successful")
vehicle.arm()
time.sleep(2)
vehicle.set_flight_mode("FBWA")


# Throttle (kalkış ve güç için kullanılabilir)
while True:
    vehicle.set_rc_channel_pwm(3, 2000)

# yaw
# 1500-3000 arası sola
# 0-1500 arası sağa
"""
while True:
    set_rc_channel_pwm(4,1500)
"""

# pitch
# 1500-3000 arası sola
# 0-1500 arası sağa
"""
while True:
    set_rc_channel_pwm(1,3000)
"""

# roll baş yukarı aşağı ayarlama
"""
while True:
    set_rc_channel_pwm(2, 0)
"""