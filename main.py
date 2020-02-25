import time
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QPushButton, QHBoxLayout, QVBoxLayout, QProgressBar, QLabel, QAction
from PyQt5.QtGui import QIcon, QPixmap
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
        self.label1.setText("Скорость относительно земли")
        self.label1.move(5,2)
        self.label1.resize(250,20)
        
        self.label2 = QLabel(self)
        self.label2.setText("Скорость относительно воздуха")
        self.label2.move(225,2)
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
           
    def my_func(self):

        self.startbutton.move(2222,2222)
        #print(self.startbutton.isEnabled)
        
        
    def my_func2(self):
        self.startbutton.move(370, 520)
        self.finishbutton.isVisible = False
        

    def _countdown(self):
         
         for i in range(0,100000000):
             x = vehicle.groundspeed
             y = vehicle.airspeed
        
             time.sleep(0.02)
             #print(x)
             self.lcdnumber.display(x)
             self.lcdnumber2.display(y)
             self.progressBar.setValue(vehicle.battery.level)
             
             
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()


