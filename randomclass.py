import random
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-darkgrid')

x = []
y = []

def animate(i):
    with open('data.csv', newline='') as csvfile:
        x = []
        y = []
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for (j,row) in enumerate(spamreader):
            x.append(j/2)
            y_value = row.count(str(0)) / len(row)
            y.append(y_value*100)
    plt.cla()
    
    plt.plot(x, y, label='Concentration')
    plt.title("Student’s Concentration Estimation System")
    plt.xlabel('Time')

    
    plt.legend(loc='lower right')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=2000)
plt.tight_layout()
plt.show()