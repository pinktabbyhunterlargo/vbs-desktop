import sys
from playsound import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   vbs = QPushButton(widget)
   vbs.setText("vine boom sfx")
   vbs.move(10,10)
   vbs.clicked.connect(vbs_clicked)

   eof = QPushButton(widget)
   eof.setText("e05 momen")
   eof.move(10,40)
   eof.clicked.connect(eof_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("vbs desktop pyqt5 test")
   widget.show()
   sys.exit(app.exec_())


def vbs_clicked():
    playsound('files/Vine-boom-sound-effect.mp3')

def eof_clicked():
    playsound('files/E05-alt.mp3')
   
if __name__ == '__main__':
   window()
