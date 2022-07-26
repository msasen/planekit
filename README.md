# Getting Started

Planekit helps you create powerful apps for **fixed-wing** UAVs. These apps run on a UAV’s Companion Computer, and augment the autopilot by performing tasks that are both computationally intensive and require a low-latency link.

This documentation provides everything you need to get started with Planekit, including an overview of the API, quick start, guide material, a number of demos and examples, and API Reference.

## Install Planekit

```
pip install planekit
```

# Start simulation anywhere or connect UAV:

Plankit does not include any built-in simulation. Therefore, you must connect the planekit still or an arduplane installed UAV.

A simple example of starting a still with Mission planar

![image info](https://aybars-510d8.web.app/assets/images/Misson_plannar-4d87924f4fe68d22243335134c90184b.png)

Planekit supports other alternatives. (Mavproxy etc.)
## First connection

You can see the first connection example below.


```jsx title="commonly_used_data"
import time

import planekit

vehicle = planekit.Connection("tcp:127.0.0.1:5762")
vehicle.wait_heartbeat()
print("connection is successful")
```
# See Docs
https://plane-kit.com/