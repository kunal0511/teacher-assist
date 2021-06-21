import webbrowser
import os
from PyQt5 import QtWidgets , uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import  *
import sys
import datetime
from block_websites import *

block()

def startMeeting():
    global startTime
    startTime = datetime.now().replace(microsecond = 0)
    print("Start Time is : ",startTime)
    openBrowser()
    
def endMeeting():
    global endTime
    endTime = datetime.now().replace(microsecond = 0)
    print("End Time is : ",endTime)
    attendance()
    leave()
    

def openBrowser():
    url = 'https://meet.google.com/tat-esdq-vcb'
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new(url)
    button2.setEnabled(True)
    button1.setEnabled(False)
    
def leave(): 
    browserExe = "chrome.exe" 
    os.system("taskkill /f /im "+browserExe)
    win.close()
    
def attendance():
    print("Total minutes Attended : ",endTime - startTime)

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400, 400, 640, 300)
win.setWindowTitle("Join Meeting")

label = QtWidgets.QLabel(win)
label.setText("Enter Name : \n\nEnter Roll no: ")
label.setFont(QFont('Sans Serif', 20))
label.adjustSize()
label.move(50, 50)

line = QtWidgets.QLineEdit(win)
line.move(280,56)
line.setFixedWidth(200)
line.setFixedHeight(40)
line.setFont(QFont('Roboto', 15))

line2 = QtWidgets.QLineEdit(win)
line2.move(280,140)
line2.setFixedWidth(200)
line2.setFixedHeight(40)
line2.setFont(QFont('Roboto', 15))

button1 = QtWidgets.QPushButton(win)
button1.setText("Start Meeting")
button1.setFont(QFont('Roboto', 12))
button1.clicked.connect(startMeeting)
button1.resize(140,50)
button1.move(170,215)

button2 = QtWidgets.QPushButton(win)
button2.setText("End Meeting")
button2.setFont(QFont('Roboto', 12))
button2.clicked.connect(endMeeting)
button2.resize(140,50)
button2.move(380,215)
button2.setEnabled(False)

win.show()
sys.exit(app.exec_())

