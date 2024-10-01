import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  
        close_index = headers.index("Close/Last") 
        for row in reader:
            close_value = float(row[close_index].replace(',', ''))
            data.append(close_value) 
    return data[::-1]

file_path = "sp2.csv"
close_data = read_csv_file(file_path)

max_investment = 50000
min_investment = -50000
num_1 = 12
investment_1 = -(num_1 * close_data[0])
num_2 = 0
investment_2 = 0
num_3 = 0
investment_3 = 0

#buy on down days
def strat_1(idx):
    global num_1, investment_1
    num_0 = num_1
    day1 = close_data[idx - 1]
    day2 = close_data[idx]
    day3 = close_data[idx + 1]
    
    if num_1 * day2 < max_investment and day1 > day2:
        for i in range(3):
            if (((num_1 + 1) * day2) < max_investment):
                num_1 += 1
    elif (num_1 * day2 > min_investment):
        num_1 -= 1

    gain = -(num_1-num_0) * day3
    gain += (50000 - num_1 * day2) * (0.04 / 365)
    #print(day3, day2, day1, num_1, num_0, gain, ((50000-(num_1 * day2)) * (0.04/365)))
    investment_1 += gain

#buy at the start
def strat_2(idx):
    global num_2, investment_2
    num_0 = num_2
    day1 = close_data[idx - 1]
    day2 = close_data[idx]
    gain = num_2 * day2 - num_0 * day1
    investment_2 += gain

#sell at a certain gain, buy at a certain loss
def strat_3(idx):
    global num_3, investment_3
    num_0 = num_3
    day1 = close_data[idx - 1]
    day2 = close_data[idx]
    gain = num_3 * day2 - num_0 * day1
    investment_3 += gain

for i in range(1, len(close_data) - 1):
    strat_1(i)
    strat_2(i)
    strat_3(i)


print("DEFAULT: " + str(-50000 + 50000/close_data[0] * close_data[len(close_data)-1]))

print("STRAT 1: " + str(investment_1 + num_1 * close_data[len(close_data)-1]))
print(investment_2)
print(investment_3)
