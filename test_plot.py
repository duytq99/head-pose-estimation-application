from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import logo_rc
import random
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('test.ui', self)
        with open('data.csv', newline='') as csvfile:
            x = []
            y = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for (j,row) in enumerate(spamreader):
                x.append(j/2)
                y_value = row.count(str(0)) / len(row)
                y.append(y_value*100)
            self.plot(x, y,label='Concentration')

    #def plot(self, hour, temperature):
    #    self.graphWidget.plot(hour, temperature)

    def plot(self,x,y,label):
        plt.cla()   
        #plt.plot(x, y, label='Concentration')
        self.graphWidget.setBackground('w')
        self.graphWidget.plot(x,y,label='Concentration')

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main()