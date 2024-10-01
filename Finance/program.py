import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

max_size = 25
data = []
trading_day = 0

with open("s&p.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        trading_day += 1
        daily = []
        full_date = str(row[0])
        date = datetime.strptime(full_date, '%m/%d/%y').date()
        if trading_day > int(date.strftime('%d')):
            trading_day = 1
        open = float(row[1])
        close = float(row[4])
        data.append([trading_day, open, close]) 
    
hashmap = {}
occurances = {}

for i in range (1, max_size + 1):
    hashmap[i] = 0
    occurances[i] = 0

average = 0

for row in data:
    if row[0] == 1:
        occurances[max_size] += 1
        final_avg = hashmap[max_size]
        final_avg *= (occurances[max_size] - 1)
        final_avg += average
        final_avg /= occurances[max_size]
        hashmap[max_size] = final_avg
     
    index = row[0]
    average = (row[2]-row[1])/row[1]
    date = int(index) 
    occurances[date] += 1
    current_avg = hashmap[date]
    current_avg *= (occurances[date] - 1)
    current_avg += average
    current_avg /= occurances[date]
    hashmap[date] = current_avg
    
def percent_formatter(x, pos):
    return '{:.2f}%'.format(x * 100)

keys = list(hashmap.keys())
values = list(hashmap.values())
bars = plt.bar(keys, values, color='blue')
bars[-1].set_color('red')
plt.xlabel('Trading Day')
plt.ylabel('Average Earnings (Per Day)')
plt.title('Market Returns By Trading Day')
plt.gca().yaxis.set_major_formatter(FuncFormatter(percent_formatter))
plt.show()