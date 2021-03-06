# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selecttime.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QGraphicsView
import pialarm

global hour, minute, ampm
hour = ''
minute = ''
ampm = ''

time1 = ''
time2 = ''
time3 = ''
time4 = ''
time5 = ''

alarmtime1 = ''
alarmtime2 = ''
alarmtime3 = ''
alarmtime4 = ''
alarmtime5 = ''
class Ui_Form(object):
    def openProgram(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = program.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Form.setWindowFlags(flags)
        qtRectangle = Form.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        Form.move(qtRectangle.topLeft())
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Alarm/timeselectorbg.png"))
        self.label.setObjectName("label")
        
        self.alarmDone = QtWidgets.QPushButton(Form)
        self.alarmDone.setGeometry(QtCore.QRect(148, 475, 246, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.alarmDone.setFont(font)
        self.alarmDone.setObjectName("alarmDone")

        self.alarmDone.clicked.connect(self.getalarm)
        self.alarmDone.clicked.connect(Form.hide)
        #self.alarmDone.clicked.connect(self.openProgram)
        
        self.hour2 = QtWidgets.QPushButton(Form)
        self.hour2.setGeometry(QtCore.QRect(782, 30, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour2.setFont(font)
        self.hour2.setObjectName("hour2")

        self.hour2.clicked.connect(self.clicked_hour2)

        self.hour3 = QtWidgets.QPushButton(Form)
        self.hour3.setGeometry(QtCore.QRect(852, 30, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour3.setFont(font)
        self.hour3.setObjectName("hour3")

        self.hour3.clicked.connect(self.clicked_hour3)

        self.hour4 = QtWidgets.QPushButton(Form)
        self.hour4.setGeometry(QtCore.QRect(922, 30, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour4.setFont(font)
        self.hour4.setObjectName("hour4")

        self.hour4.clicked.connect(self.clicked_hour4)

        self.hour5 = QtWidgets.QPushButton(Form)
        self.hour5.setGeometry(QtCore.QRect(712, 100, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour5.setFont(font)
        self.hour5.setObjectName("hour5")

        self.hour5.clicked.connect(self.clicked_hour5)

        self.hour1 = QtWidgets.QPushButton(Form)
        self.hour1.setEnabled(True)
        self.hour1.setGeometry(QtCore.QRect(712, 30, 68, 68))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour1.sizePolicy().hasHeightForWidth())
        self.hour1.setSizePolicy(sizePolicy)
        self.hour1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hour1.setFont(font)
        self.hour1.setIconSize(QtCore.QSize(16, 16))
        self.hour1.setObjectName("hour1")

        self.hour1.clicked.connect(self.clicked_hour1)
        #self.hour1.clicked.connect(self.retranslateUi)

        self.hour6 = QtWidgets.QPushButton(Form)
        self.hour6.setGeometry(QtCore.QRect(782, 100, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour6.setFont(font)
        self.hour6.setObjectName("hour6")

        self.hour6.clicked.connect(self.clicked_hour6)

        self.hour7 = QtWidgets.QPushButton(Form)
        self.hour7.setGeometry(QtCore.QRect(852, 100, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour7.setFont(font)
        self.hour7.setObjectName("hour7")

        self.hour7.clicked.connect(self.clicked_hour7)

        self.hour10 = QtWidgets.QPushButton(Form)
        self.hour10.setGeometry(QtCore.QRect(782, 170, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour10.setFont(font)
        self.hour10.setObjectName("hour10")

        self.hour10.clicked.connect(self.clicked_hour10)

        self.hour8 = QtWidgets.QPushButton(Form)
        self.hour8.setGeometry(QtCore.QRect(922, 100, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour8.setFont(font)
        self.hour8.setObjectName("hour8")

        self.hour8.clicked.connect(self.clicked_hour8)

        self.hour9 = QtWidgets.QPushButton(Form)
        self.hour9.setGeometry(QtCore.QRect(712, 170, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour9.setFont(font)
        self.hour9.setObjectName("hour9")

        self.hour9.clicked.connect(self.clicked_hour9)

        self.hour11 = QtWidgets.QPushButton(Form)
        self.hour11.setGeometry(QtCore.QRect(852, 170, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour11.setFont(font)
        self.hour11.setObjectName("hour11")

        self.hour11.clicked.connect(self.clicked_hour11)

        self.hour12 = QtWidgets.QPushButton(Form)
        self.hour12.setGeometry(QtCore.QRect(922, 170, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.hour12.setFont(font)
        self.hour12.setObjectName("hour12")

        self.hour12.clicked.connect(self.clicked_hour12)

        self.minute05 = QtWidgets.QPushButton(Form)
        self.minute05.setGeometry(QtCore.QRect(782, 274, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute05.setFont(font)
        self.minute05.setObjectName("minute05")

        self.minute05.clicked.connect(self.clicked_minute05)

        self.minute20 = QtWidgets.QPushButton(Form)
        self.minute20.setGeometry(QtCore.QRect(712, 344, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute20.setFont(font)
        self.minute20.setObjectName("minute20")

        self.minute20.clicked.connect(self.clicked_minute20)

        self.minute00 = QtWidgets.QPushButton(Form)
        self.minute00.setEnabled(True)
        self.minute00.setGeometry(QtCore.QRect(712, 274, 68, 68))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minute00.sizePolicy().hasHeightForWidth())
        self.minute00.setSizePolicy(sizePolicy)
        self.minute00.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.minute00.setFont(font)
        self.minute00.setIconSize(QtCore.QSize(16, 16))
        self.minute00.setObjectName("minute00")

        self.minute00.clicked.connect(self.clicked_minute00)

        self.minute45 = QtWidgets.QPushButton(Form)
        self.minute45.setGeometry(QtCore.QRect(782, 414, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute45.setFont(font)
        self.minute45.setObjectName("minute45")

        self.minute45.clicked.connect(self.clicked_minute45)

        self.minute35 = QtWidgets.QPushButton(Form)
        self.minute35.setGeometry(QtCore.QRect(922, 344, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute35.setFont(font)
        self.minute35.setObjectName("minute35")

        self.minute35.clicked.connect(self.clicked_minute35)

        self.minute50 = QtWidgets.QPushButton(Form)
        self.minute50.setGeometry(QtCore.QRect(852, 414, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute50.setFont(font)
        self.minute50.setObjectName("minute46")

        self.minute50.clicked.connect(self.clicked_minute50)

        self.minute30 = QtWidgets.QPushButton(Form)
        self.minute30.setGeometry(QtCore.QRect(852, 344, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute30.setFont(font)
        self.minute30.setObjectName("minute30")

        self.minute30.clicked.connect(self.clicked_minute30)

        self.minute25 = QtWidgets.QPushButton(Form)
        self.minute25.setGeometry(QtCore.QRect(782, 344, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute25.setFont(font)
        self.minute25.setObjectName("minute25")

        self.minute25.clicked.connect(self.clicked_minute25)

        self.minute55 = QtWidgets.QPushButton(Form)
        self.minute55.setGeometry(QtCore.QRect(922, 414, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute55.setFont(font)
        self.minute55.setObjectName("minute55")

        self.minute55.clicked.connect(self.clicked_minute55)

        self.minute15 = QtWidgets.QPushButton(Form)
        self.minute15.setGeometry(QtCore.QRect(922, 274, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute15.setFont(font)
        self.minute15.setObjectName("minute15")

        self.minute15.clicked.connect(self.clicked_minute15)

        self.minute10 = QtWidgets.QPushButton(Form)
        self.minute10.setGeometry(QtCore.QRect(852, 274, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute10.setFont(font)
        self.minute10.setObjectName("minute10")

        self.minute10.clicked.connect(self.clicked_minute10)

        self.minute40 = QtWidgets.QPushButton(Form)
        self.minute40.setGeometry(QtCore.QRect(712, 414, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.minute40.setFont(font)
        self.minute40.setObjectName("minute40")

        self.minute40.clicked.connect(self.clicked_minute40)

        self.buttonPM = QtWidgets.QPushButton(Form)
        self.buttonPM.setGeometry(QtCore.QRect(887, 515, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.buttonPM.setFont(font)
        self.buttonPM.setObjectName("buttonPM")

        self.buttonPM.clicked.connect(self.clicked_pm)

        self.buttonAM = QtWidgets.QPushButton(Form)
        self.buttonAM.setGeometry(QtCore.QRect(747, 515, 68, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.buttonAM.setFont(font)
        self.buttonAM.setObjectName("buttonAM")

        self.buttonAM.clicked.connect(self.clicked_am)

        self.labelAMPM = QtWidgets.QLabel(Form)
        self.labelAMPM.setGeometry(QtCore.QRect(765, 482, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        self.labelAMPM.setFont(font)
        self.labelAMPM.setObjectName("labelAMPM")
        
        self.labelMinute = QtWidgets.QLabel(Form)
        self.labelMinute.setGeometry(QtCore.QRect(765, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(19)
        self.labelMinute.setFont(font)
        self.labelMinute.setObjectName("labelMinute")
        
        self.labelHour = QtWidgets.QLabel(Form)
        self.labelHour.setGeometry(QtCore.QRect(765, -2, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(19)
        self.labelHour.setFont(font)
        self.labelHour.setObjectName("labelHour")
        
        self.labelDisplayTime = QtWidgets.QLabel(Form)
        self.labelDisplayTime.setGeometry(QtCore.QRect(100, 60, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(46)
        self.labelDisplayTime.setFont(font)
        self.labelDisplayTime.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelDisplayTime.setObjectName("labelDisplayTime")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hour2.setText(_translate("Form", "2"))
        self.hour3.setText(_translate("Form", "3"))
        self.hour4.setText(_translate("Form", "4"))
        self.hour5.setText(_translate("Form", "5"))
        self.hour1.setText(_translate("Form", "1"))
        self.hour6.setText(_translate("Form", "6"))
        self.hour7.setText(_translate("Form", "7"))
        self.hour10.setText(_translate("Form", "10"))
        self.hour8.setText(_translate("Form", "8"))
        self.hour9.setText(_translate("Form", "9"))
        self.hour11.setText(_translate("Form", "11"))
        self.hour12.setText(_translate("Form", "12"))
        self.minute05.setText(_translate("Form", "05"))
        self.minute20.setText(_translate("Form", "20"))
        self.minute00.setText(_translate("Form", "00"))
        self.minute45.setText(_translate("Form", "45"))
        self.minute35.setText(_translate("Form", "35"))
        self.minute50.setText(_translate("Form", "50"))
        self.minute30.setText(_translate("Form", "30"))
        self.minute25.setText(_translate("Form", "25"))
        self.minute55.setText(_translate("Form", "55"))
        self.minute15.setText(_translate("Form", "15"))
        self.minute10.setText(_translate("Form", "10"))
        self.minute40.setText(_translate("Form", "40"))
        self.buttonPM.setText(_translate("Form", "PM"))
        self.buttonAM.setText(_translate("Form", "AM"))
        self.labelAMPM.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt; font-weight:600;\">Select AM/PM</span></p></body></html>"))
        self.labelMinute.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt; font-weight:600;\">Select Minute</span></p></body></html>"))
        self.labelHour.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt; font-weight:600;\">Select Hour</span></p></body></html>"))
        self.labelDisplayTime.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
        self.alarmDone.setText(_translate("Form", "Set Alarm"))

    def clicked_hour1(self):
        global hour
        hour = '1'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))

    def clicked_hour2(self):
        global hour
        hour = '2'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour3(self):
        global hour
        hour = '3'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour4(self):
        global hour
        hour = '4'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour5(self):
        global hour
        hour = '5'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour6(self):
        global hour
        hour = '6'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour7(self):
        global hour
        hour = '7'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour8(self):
        global hour
        hour = '8'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour9(self):
        global hour
        hour = '9'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour10(self):
        global hour
        hour = '10'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour11(self):
        global hour
        hour = '11'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_hour12(self):
        global hour
        hour = '12'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute00(self):
        global minute
        minute = ':' + '00'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute05(self):
        global minute
        minute = ':' + '05'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute10(self):
        global minute
        minute = ':' + '10'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute15(self):
        global minute
        minute = ':' + '15'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute20(self):
        global minute
        minute = ':' + '20'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute25(self):
        global minute
        minute = ':' + '25'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute30(self):
        global minute
        minute = ':' + '30'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute35(self):
        global minute
        minute = ':' + '35'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute40(self):
        global minute
        minute = ':' + '40'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute45(self):
        global minute
        minute = ':' + '45'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute50(self):
        global minute
        minute = ':' + '50'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_minute55(self):
        global minute
        minute = ':' + '55'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_am(self):
        global ampm
        ampm = 'AM'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))
    def clicked_pm(self):
        global ampm
        ampm = 'PM'
        _translate = QtCore.QCoreApplication.translate
        self.labelDisplayTime.setText(_translate("Form",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:46pt;\">"+ hour + minute + " " + ampm +"</span></p></body></html>"))

    def getalarm(self):

        global alarmtime1, alarmtime2, alarmtime3, alarmtime4, alarmtime5
        if alarmtime1 == '':
            alarmtime1 = hour + minute + ":00 " + ampm
            global time1
            time1 = hour + minute + ' ' + ampm
        elif alarmtime2 == '':
            global time2
            alarmtime2 = hour + minute + ":00 " + ampm
            time2 = hour + minute + ' ' + ampm
        elif alarmtime3 == '':
            global time3
            alarmtime3 = hour + minute + ":00 " + ampm
            time3 = hour + minute + ' ' + ampm
        elif alarmtime4 == '':
            global time4
            alarmtime4 = hour + minute + ":00 " + ampm
            time4 = hour + minute + ' ' + ampm
        else:
            global time5
            alarmtime5 = hour + minute + ":00 " + ampm
            time5 = hour + minute + ' ' + ampm

    def clicked_done(self):
        print(hour)
        print(minute)
        print(ampm)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setCursor(QtCore.Qt.BlankCursor)
    Form.showFullScreen()
    sys.exit(app.exec_())
