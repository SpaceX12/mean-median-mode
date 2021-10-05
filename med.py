import csv
#import numpy

with open('HeightWeight.csv', newline='') as o:
    e = csv.reader(o)
    data = list(e)
    
data.pop(0)

weight = []
for i in range(len(data)):
    weight.append(float(data[i][2]))

w = len(data)
weight.sort()

if w%2 == 0:
    e1 = weight[1//2]
    e2 = weight[1//2 - 1]
    md = (1+2)/2
else:
    md = weight/2

#med = numpy.median(weight)

print('Middle Weight is:' + str(md))