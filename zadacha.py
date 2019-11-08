import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Приветик!')

        self.button = QPushButton('Жмяк!', self)
        self.button.resize(100, 100)
        self.button.move(350, 350)
        self.button.clicked.connect(self.run)
        
    def run(self):
        self.flag = True        
        
    def paintEvent(self, event):
        if self.flag:        
            self.qp = QPainter()
            self.qp.begin(self)
            #self.draw(self)
            a = (random.randint(50, 200))
            self.qp.setBrush(QColor(random.randint(0, 255), 
                                                   random.randint(0, 255), 
                                                   random.randint(0, 255)))
            self.qp.drawEllipse(random.randint(50, 600), 
                                random.randint(50, 600), a, a)
            self.qp.end()  
            self.update()
            
            
    def draw(self):
        self.b = random.randint(10, 250)
        print(self.b)
        self.c = random.randint(10, 250)
        print(self.c)
        self.qp.setBrush(QColor(100, 100, 0))   
        a = random.randint(10, 300)
        self.qp.drawEllipse(*[self.b, self.c], a, a)   
         
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
