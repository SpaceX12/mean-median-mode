import csv
#from scipy import stats
from collections import Counter

with open('HeightWeight.csv', newline='') as o:
    e = csv.reader(o)
    data = list(e)
    
data.pop(0)

weight = []
for i in range(len(data)):
    weight.append(float(data[i][2]))

data = Counter(weight)

data_r ={
    '90-100':0,
    '100-110':0,
    '110-120':0,
    '120-130':0,
    '130-140':0,
    '140-150':0,
    '150-160':0,
}

for weight,occurance in data.items():
    if 90<weight<100:
        data_r["90-100"] += occurance
    elif 100<weight<110:
        data_r["100-110"] += occurance
    elif 110<weight<120:
        data_r["110-120"] += occurance
    elif 120<weight<130:
        data_r["120-130"] += occurance
    elif 130<weight<140:
        data_r["130-140"] += occurance
    elif 140<weight<150:
        data_r["140-150"] += occurance
    elif 150<weight<160:
        data_r["150-160"] += occurance 

m_r, m_o = 0,0

for range,occurance in data_r.items():
    if occurance>m_o:
        m_r,m_o = [int(range.split('-')[0]), int(range.split('-')[1])], occurance

mod = float((m_r[0]+m_r[1])/2)

#d = stats.mode(weight)

print('Most Common Weight Is:' + str(mod))