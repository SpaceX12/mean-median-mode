import csv
#import numpy

with open('HeightWeight.csv', newline='') as o:
    e = csv.reader(o)
    data = list(e)
    
data.pop(0)

weight = []
for i in range(len(data)):
    weight.append(float(data[i][2]))

#avg2 = numpy.mean(weight)

q = len(data)
s = 0

for i in weight:
    s = s + i

avg = s/q

print('Average Weight is:' + str(avg))