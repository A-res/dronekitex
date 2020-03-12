import asyncio
from mavsdk import System


async def run():

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()
    
import time
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QLineEdit, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QProgressBar, QLabel, QAction 
from PyQt5.QtGui import QIcon, QPixmap
print("starting sim") 
import dronekit_sitl
sitl =  dronekit_sitl.start_default()
connection_string       = 'udpin:127.0.0.1:14550'
import design
from dronekit import connect, VehicleMode 
#import main2

print("Connection to vehicle", connection_string)
vehicle = connect(connection_string, wait_ready=True)
print(vehicle.rangefinder)
#print(vehicle.capabilities)
print(vehicle.channels)
print(vehicle.heading)
print(vehicle.velocity)
print(vehicle.gps_0)
print(vehicle.gimbal)
print(vehicle.airspeed)
class Window(QMainWindow, design.Ui_aBPLA):

    def __init__(self):
        QMainWindow.__init__(self)
        self.startbutton = QPushButton(self)
        self.startbutton.clicked.connect(self.my_func)
        self.startbutton.clicked.connect(self.threadstart)
        self.startbutton.move(370, 520)
        self.startbutton.setText('Начать симуляцию')
        self.startbutton.resize(200,50)
        #self.act = QAction(self)
       
       # self.startbutton.addAction(self.act)  
        #self.act.is_clicked.connect(self.my_func)
        self.progressBar = QProgressBar(self)
        self.progressBar.move(20,100)
        self.progressBar.resize(400,30)
        
        self.finishbutton = QPushButton(self)
        self.finishbutton.clicked.connect(self.my_func2)
        self.finishbutton.clicked.connect(self.threadstart)
        self.finishbutton.move(160, 520)
        self.finishbutton.setText('Прекратить симуляцию')
        self.finishbutton.resize(200,50)
        
        self.takeoffbutton = QPushButton(self)
        self.takeoffbutton.clicked.connect(self.my_func)
        self.takeoffbutton.clicked.connect(self.threadstart)
        self.takeoffbutton.move(20, 160)
        self.takeoffbutton.setText('takeoffbutton')
        
        self.takeoffbutton.resize(200,50)
       
        self.decor = QGroupBox(self)
        self.decor.move(0,240)
        self.decor.resize(240, 90)
        
        print(vehicle.location.global_relative_frame)
        print(vehicle.location.global_frame)
        
        #print(k)
        self.location = QLabel(self)
        self.location.move(0, 260)
        #self.location.setText(k)
        self.location.resize(800, 20)    
        
        self.head = QLabel(self)
        self.head.move(1, 350)
        self.location.resize(800, 60)         
         
        self.landbutton = QPushButton(self)
        self.landbutton.clicked.connect(self.my_func)
        self.landbutton.clicked.connect(self.threadstart)
        self.landbutton.move(220, 160)
        self.landbutton.setText('takeoffbutton')
        self.landbutton.resize(200,50)
       
        self.lcdnumber = QLCDNumber(self)
        self.lcdnumber.resize(190, 50) 
        self.lcdnumber.move(20,20)
        self.lcdnumber2 = QLCDNumber(self)
        self.lcdnumber2.resize(190, 50) 
        self.lcdnumber2.move(230,20)
        
        self.resize(600, 600)
       
        self.label = QLabel(self)
        self.label.resize(300,300)
        self.label.move(445,-85)
        
        self.label1 = QLabel(self)
        self.label1.setText("Скорость относительно земли м/с")
        self.label1.move(5,2)
        self.label1.resize(250,20)
        
        self.label2 = QLabel(self)
        self.label2.setText("_yawspeed")
        self.label2.move(285,2)
        self.label2.resize(250,20)
        
        self.label3 = QLabel(self)
        self.label3.setText("Заряд батареи в %")
        self.label3.move(150,75)
        self.label3.resize(250,20)
        
        pixmap = QPixmap('/home/ppz/image.jpg')
        self.label.setPixmap(pixmap)
        
        
    def threadstart(self):
        t = Thread(target=self._countdown)
        t.start()     
        if self.finishbutton.isVisible == False:
           t.join()
           #window.
    def my_func(self):

        self.startbutton.move(2222,2222)
        #print(self.startbutton.isEnabled)
        
        
    def my_func2(self):
        self.startbutton.move(370, 520)
        self.finishbutton.isVisible = False
        

    def _countdown(self):
         
         for i in range(0,100000000):
             
             north=str(vehicle.location.local_frame.north)
             east=str(vehicle.location.local_frame.east)
             down=str(vehicle.location.local_frame.down)
             h=str(vehicle._heading)
             x = vehicle._groundspeed
             y = vehicle._yawspeed
            # 
             self.location.setText("north = " + north + "\n" + "east = " + east + "\n" + "down = " + down)
             self.head.setText("heading = " + h + "°")
            # time.sleep(0.002)
             self.lcdnumber.display(x)
             #time.sleep(0.42)
             self.lcdnumber2.display(y)
         #    self.send_mavlink("commander takeoff")
            # print(k)
             
             self.progressBar.setValue(vehicle.battery.level)
          
                     
           #  print("-- Arming")
            
             
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()


