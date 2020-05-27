
import csv
import random
import time

stu_num = 50
fieldnames = []
row=[]
for i in range(50):
    fieldnames.append("SV"+str(i))
print(fieldnames)

with open('data.csv', 'w', newline='') as csvfile:
    chinh = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    chinh.writerow(fieldnames)

while True:

    with open('data.csv', 'a') as csvfile:
        chinh = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(50):
            row.append(str(random.randint(0,1)))
        chinh.writerow(row)
        row=[]

    time.sleep(2)
