#import asyncio  
#from mavsdk import System   // две строчки на случай использования mavsdk для отправления команд на дрон, но в последней версии все работает уже без них
import time
from threading import Thread // две строчки для подключения потоков и таймера реального времени
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QLineEdit, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QProgressBar, QLabel, QAction 
from PyQt5.QtGui import QIcon, QPixmap   //подключение библиотек qt с интерфейсами
print("starting sim") 
import dronekit_sitl
sitl =  dronekit_sitl.start_default()  // подключение библиотек для работы с дроном либо симуляцией дрона по mavlink
connection_string       = 'udpin:127.0.0.1:14550' //запуск соединения на порту, который прописан в консоли при запуске mavlink
import design
from dronekit import connect, VehicleMode  //основной класс дронкита 
print("Connection to vehicle", connection_string) //вывод статуса подключения
vehicle = connect(connection_string, wait_ready=True) //ожидание подключения
print(vehicle.rangefinder)  // ) 
#print(vehicle.capabilities)// |
print(vehicle.channels)     // |
print(vehicle.heading)      // |
print(vehicle.velocity)     // > функции основного класса дронкита для вывода в консоль основных полетных характеристик устройства, 
print(vehicle.gps_0)        // | подсоединенного по мавлинку
print(vehicle.gimbal)       // |
print(vehicle.airspeed)     // )
class Window(QMainWindow, design.Ui_aBPLA): //класс основного окна интерфейса

    def __init__(self):                
        QMainWindow.__init__(self) //иницилизация 
        self.startbutton = QPushButton(self) 
        self.startbutton.clicked.connect(self.my_func)
        self.startbutton.clicked.connect(self.threadstart)
        self.startbutton.move(370, 520)
        self.startbutton.setText('Начать симуляцию')
        self.startbutton.resize(200,50)
        #self.act = QAction(self)                           //отрисовка кнопки старт
       
       # self.startbutton.addAction(self.act)  
        #self.act.is_clicked.connect(self.my_func)
        self.progressBar = QProgressBar(self)
        self.progressBar.move(20,100)
        self.progressBar.resize(400,30)                      //отрисовка прогрессбара
        
        self.finishbutton = QPushButton(self)
      #  self.finishbutton.clicked.connect(self.my_func2)
        self.finishbutton.clicked.connect(self.threadstart)
        self.finishbutton.move(160, 520)
        self.finishbutton.setText('Прекратить симуляцию')
        self.finishbutton.resize(200,50)					//отрисовка кнопки стоп
        
        self.takeoffbutton = QPushButton(self)					//отрисовка кнопки взлета (пока не привязана к команде)
   #     self.takeoffbutton.clicked.connect(self.my_func2)
      #  self.takeoffbutton.clicked.connect(self.threadstart)
        self.takeoffbutton.move(20, 160)
        self.takeoffbutton.setText('takeoffbutton')
        
        self.takeoffbutton.resize(200,50)
       
        self.decor = QGroupBox(self)
        self.decor.move(130,240)
        self.decor.resize(260, 90)		//отрисовка декоративных элементов
        
        print(vehicle.location.global_relative_frame)
        print(vehicle.location.global_frame)    //вывод в консоль абсолютного и относительного положения объекта висящего на мавлинке
        
        #print(k)
        self.location = QLabel(self)	
        self.location.move(150, 260)
        #self.location.setText(k)
        self.location.resize(800, 20)    //отрисовка подписей
        
        self.head = QLabel(self)
        self.head.move(130, 350)
        self.location.resize(800, 60)          //отрисовка подписей
         
        self.landbutton = QPushButton(self)
        self.landbutton.clicked.connect(self.my_func)
        self.landbutton.clicked.connect(self.threadstart)
        self.landbutton.move(220, 160)
        self.landbutton.setText('takeoffbutton')
        self.landbutton.resize(200,50)            //отрисовка подписей
       
        self.lcdnumber = QLCDNumber(self)
        self.lcdnumber.resize(190, 50) 
        self.lcdnumber.move(20,20)
        self.lcdnumber2 = QLCDNumber(self)
        self.lcdnumber2.resize(190, 50) 
        self.lcdnumber2.move(230,20)  //отрисовка дисплеев
        
        self.resize(600, 600)
       
        self.label = QLabel(self)
        self.label.resize(300,300)    //отрисовка подписей
        self.label.move(445,-85)
        
        self.label1 = QLabel(self)
        self.label1.setText("Скорость относительно земли м/с")
        self.label1.move(5,2)
        self.label1.resize(250,20)   //отрисовка подписей
        
        self.label2 = QLabel(self)
        self.label2.setText("_yawspeed")
        self.label2.move(285,2)
        self.label2.resize(250,20)  //отрисовка подписей
        
        self.label3 = QLabel(self)
        self.label3.setText("Заряд батареи в %")
        self.label3.move(150,75)
        self.label3.resize(250,20)  //отрисовка подписей
        
        pixmap = QPixmap('/home/ppz/image.jpg')
        self.label.setPixmap(pixmap)            //эмблема ниипа
        
        
    def threadstart(self):                         //функция запуска потока по нажатию на кнопку старт
        t = Thread(target=self._countdown)
        t.start()     
        if self.finishbutton.isVisible == False:
           t.join()
           #window.
    def my_func(self):

        self.startbutton.move(2222,2222)  //кнопка старт прячется после старта до нажатия на "стоп"
        #print(self.startbutton.isEnabled)
        
     
       
            

    def _countdown(self):										//запуск таймера, относительно которого идет замер данных
         
         for i in range(0,100000000):
             
             north=str(vehicle.location.local_frame.north)   //
             east=str(vehicle.location.local_frame.east)    // считывание геокоординат в формате компаса
             down=str(vehicle.location.local_frame.down)   //
             h=str(vehicle._heading)
             x = vehicle._groundspeed
             y = vehicle._yawspeed
             vehicle.arm(self)              //команда: объект на мавлинке заряжен
             vehicle.simple_takeoff(1115)   //команда: объект взлетает на заданную высоту. в том же классе vehicle можно установить и 
            # 								пункт назначения в формате координат места
             self.location.setText("north = " + north + "\n" + "east = " + east + "\n" + "down = " + down) //компас (только текст)
             self.head.setText("heading = " + h + "°") //направление
            # time.sleep(0.002)				//задержка таймера для корректного отображения на дисплеях
             self.lcdnumber.display(x)
             #time.sleep(0.42)
             self.lcdnumber2.display(y)
         #    self.send_mavlink("commander takeoff")		
            # print(k)
             
             self.progressBar.setValue(vehicle.battery.level) //заполнение прогрессбара
          
                     
           #  print("-- Arming")
            
             
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()


