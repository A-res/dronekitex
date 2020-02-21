import time
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QPushButton, QHBoxLayout, QVBoxLayout, QProgressBar
print("starting sim") 
import dronekit_sitl
sitl =  dronekit_sitl.start_default()
connection_string       = 'udpin:127.0.0.1:14550'
import design
from dronekit import connect, VehicleMode 

print("Connection to vehicle", connection_string)
vehicle = connect(connection_string, wait_ready=True)

class Window(QMainWindow, design.Ui_aBPLA):

    def __init__(self):
        QMainWindow.__init__(self)
        self.lcdnumber = QLCDNumber(self)
        self.lcdnumber.move(20,20)
        self.lcdnumber2 = QLCDNumber(self)
        self.lcdnumber2.move(300,20)
        self.progressBar = QProgressBar(self)
        self.progressBar.move(80,80)
        self.resize(600, 600)
        t = Thread(target=self._countdown)
        t.start()
        
        
   

    def _countdown(self):
         
         for i in range(0,100000000):
             x = vehicle.groundspeed
             y = vehicle.airspeed
        
             time.sleep(0.02)
             print(x)
             self.lcdnumber.display(x)
             self.lcdnumber2.display(y)
             self.progressBar.setValue(vehicle.battery.level)
             
             
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()


