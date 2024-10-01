import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

file_path = "s&p return.csv"
data_array = read_csv_file(file_path)

# Printing the data array
for row in data_array:
    print(row)
