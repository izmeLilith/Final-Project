import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon


class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3>2 X 2 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(155, 25)
        self.setWindowIcon(QIcon('custom.ico'))
       

        self.setWindowTitle("2 x 2 Determinant Window")
        self.setGeometry(500, 100, 500, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150,80)
        self.textbox1.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 110)
        self.textbox3.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(250, 80)
        self.textbox2.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(250, 110)
        self.textbox4.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(350, 140)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(240, 145)
        self.text.resize(120, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Submit your information")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Clear all your information")
        self.button.move(150,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(250,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('Exit', self)
        self.button.setToolTip("Exit to the System")
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        
        self.button.move(350,350)
        self.button.clicked.connect(QApplication.instance().quit)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
       

    @pyqtSlot()

    def Window_3(self):
        self.wndw3 = Window3()
        self.wndw3.show()
        Window2.close(self)

    def back(self):
        Window2.close(self)
        self.open = Window()
        self.open.show()
        


     
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.det.setText("")
    
        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        a = int(self.textbox1.text())
        b = int(self.textbox2.text())
        c = int(self.textbox3.text())
        d = int(self.textbox4.text())
        self.matrix_computation(a, b, c, d)
    
    
    

    def matrix_computation(self, a ,b ,c, d):

        Determinate = (a*d)-(b*c)
        self.det.setText(f"{Determinate}")
        
        

class Window3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> 3 X 3 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(150, 20)
        self.setWindowIcon(QIcon('custom.ico'))

        self.setWindowTitle("3 x 3 Determinant Window")
        self.setGeometry(500, 100, 500, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(380, 170)
        self.det.resize(100, 30)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(265, 175)
        self.text.resize(120, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Submit your information")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Clear all your information")
        self.button.move(150,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(250,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('Exit', self)
        self.button.setToolTip("Exit to the System")
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        
        self.button.move(350,350)
        self.button.clicked.connect(QApplication.instance().quit)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()

    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.det.setText("")
        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        a = int(self.textbox1.text())
        b = int(self.textbox2.text())
        c = int(self.textbox3.text())
        d = int(self.textbox4.text())
        e = int(self.textbox5.text())
        f = int(self.textbox6.text())
        g = int(self.textbox7.text())
        h = int(self.textbox8.text())
        i = int(self.textbox9.text())
        self.matrix_computation(a, b, c, d, e, f, g, h, i)
    
    def back(self):
        Window3.close(self)
        self.open = Window()
        self.open.show()
               

    def Window(self):
        self.nwndw = Window()
        self.nwndw.show()


    def matrix_computation(self, a ,b ,c, d, e, f, g, h, i):
        A = (a*e*i)
        B = (b*f*g)
        C = (c*d*h)
        D = (c*e*g)
        E = (a*f*h)
        F = (b*d*i)

        Determinate = (A + B + C) - (D + E + F)
        self.det.setText(f"{Determinate}")


class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> 4 X 4 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(150, 20)
        self.setWindowIcon(QIcon('custom.ico'))
       

        self.setWindowTitle("4 x 4 Determinant Window")
        self.setGeometry(600, 100, 600, 500)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(450, 200)
        self.det.resize(100, 30)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(340, 204)
        self.text.resize(120, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Submit your information")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        self.button.setToolTip("Clear all your information")
        self.button.move(150,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(250,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('Exit', self)
        self.button.setToolTip("Exit to the System")
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:#4782ff ; font: 8pt}")
        
        self.button.move(350,350)
        self.button.clicked.connect(QApplication.instance().quit)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()

    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
        self.det.setText("")
        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        a = int(self.textbox1.text())
        b = int(self.textbox2.text())
        c = int(self.textbox3.text())
        d = int(self.textbox4.text())
        e = int(self.textbox5.text())
        f = int(self.textbox6.text())
        g = int(self.textbox7.text())
        h = int(self.textbox8.text())
        i = int(self.textbox9.text())
        j = int(self.textbox10.text())
        k = int(self.textbox11.text())
        l = int(self.textbox12.text())
        m = int(self.textbox13.text())
        n = int(self.textbox14.text())
        o = int(self.textbox15.text())
        p = int(self.textbox16.text())
        paintEngine = int(self.textbox16.text())
        self.matrix_computation(a, b, c, d, e, f, g, h, i,j,k,l,m,n,o,p)
    
    def back(self):

        Window4.close(self)
        self.open = Window()
        self.open.show()

    
    
        

    def matrix_computation(self, a, b, c, d, e, f, g, h, i,j,k,l,m,n,o,p):
        A = a*((f*(k*p-l*o)) - (g*(j*p-l*n)) + (h*(j*o-k*n)))
        B = b*((e*(k*p-l*o)) - (g*(i*p-l*m)) + (h*(i*o-k*m)))
        C = c*((e*(j*p-l*n)) - (f*(i*p-l*m)) + (h*(i*n-j*m)))
        D = d*((e*(j*o-k*n)) - (f*(i*o-k*m)) + (g*(i*n-j*m)))

        Determinate = A-B+C-D
        self.det.setText(f"{Determinate}")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Matrix Calculator"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.setWindowIcon(QIcon('custom.ico'))

        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("background-color : #d67d00 ; color : white ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        
        self.pushButton.setToolTip("Start")
        
        self.pushButton.clicked.connect(self.window2)
        
        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("background-color : #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Start")
        
        self.pushButton.clicked.connect(self.window3)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("background-color : #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13 , QFont.Bold))
        self.pushButton.setToolTip("Start")
        
        self.pushButton.clicked.connect(self.window4)             
        self.main_window()

    def Window_2(self):
        self.wndw2 = Window2
        self.wndw2.show()
        self.Window.close()


    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Determinant Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(95, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()
    

    def window2(self):
        self.close()
        self.open = Window2()
        self.open.show()


    def window3(self):
        self.close()
        self.w = Window3()
        self.w.show()

    def window4(self):
        self.close()
        self.w = Window4()
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())