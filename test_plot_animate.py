import sys
import random
import matplotlib
import csv
import logo_rc
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets, uic
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('test.ui', self)
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.xdata = []
        self.ydata = []
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

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