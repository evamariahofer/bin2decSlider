#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED

leds = [LED(18),LED(23),LED(24),LED(25)]

class EvaWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setMinimumSize(QSize(600, 450))    
        self.setWindowTitle('Bit Representation with slider')
        
        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        # Slider + Label Anzeige Dezimalwert
        self.slider = QSlider(Qt.Horizontal)
        self.label = QLabel('0') 
        sliderbox = QHBoxLayout()
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.dec2bit)


        
        # Labels fuer 4 Bits
        self.bitlabels = [QLabel('8'), QLabel('4'), QLabel('2'), QLabel('1') ] # Liste
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        for bitlabel in self.bitlabels:
            bitbox.addWidget(bitlabel)
            bitlabel.setStyleSheet("background-color: grey")
            bitlabel.setFixedSize(50,50)
            bitlabel.setAlignment(QtCore.Qt.AlignCenter)

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        wid.setLayout(vbox)
        
    def dec2bit(self):
        valSlider = self.slider.value()
        self.label.setNum(valSlider)
        temp = 0
        for index, bitlabel in enumerate(self.bitlabels):
            leds[index].off()
            bitlabel.setStyleSheet("background-color: grey")
            numBit = int(bitlabel.text())
            if temp + numBit <= valSlider:
                temp += numBit
                bitlabel.setStyleSheet("background-color: red")
                leds[index].on()
                
                
        
        
app = QtWidgets.QApplication([])
win = EvaWindow()
win.show()
app.exec_()
