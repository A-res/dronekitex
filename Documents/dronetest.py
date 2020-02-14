#Howto

#1)pip3 install dronekit
#2)pip3 install dronekit-sitl
#3)pip3 install mavproxy
#4)apt-get install rosmelodic
#5)source /opt/ros/melodic/setup.bash
#6)make px4_sitl jmavsim
#7)./QGroundcontrol.appimage
#8)dronekit-sitl copter
#9)mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:1450



print("starting sim")
import dronekit_sitl
sitl =  dronekit_sitl.start_default()
connection_string = sitl.connection_string()

from dronekit import connect, VehicleMode 

print("Connection to vehicle", connection_string)
vehicle = connect(connection_string, wait_ready=True)

print("Battery:", vehicle.battery)
print("takeoff", vehicle.vehicle.arm)
print("location", vehicle.location())

#time.sleep(10)
vehicle.close()
sitl.stop() 