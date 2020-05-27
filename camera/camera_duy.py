# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

import random
import matplotlib
import csv
import logo_rc
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets, uic
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from test import *

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('test1.ui', self)
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.xdata = []
        self.ydata = []
        self.update_plot()
        self.cap = cv2.VideoCapture(0)
        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.timeout.connect(self.viewCam)

        self.timer.start()

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        # goi ham xu ly tu file khac ve => show image ra => xong
        cv2.putText(image,"CONCENTRATION",(50,100),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,255,0),thickness=2)
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.image_label.setPixmap(QPixmap.fromImage(qImg))

    def update_plot(self):
        with open('data.csv', newline='') as csvfile:
            # Drop off the first y element, append a new one.
            x = []
            y = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for (j,row) in enumerate(spamreader):
                x.append(j/2)
                y_value = row.count(str(0)) / len(row)
                y.append(y_value*100)
            self.xdata = x
            self.ydata = y
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(self.xdata, self.ydata)
            #self.MplWidget.canvas.label(xlabel = "X")
            self.MplWidget.canvas.axes.set_title('Concentration Graph')
            self.MplWidget.canvas.draw()

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
   

if __name__ == '__main__':
    main()