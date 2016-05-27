import csv
def read_write_csv(readwrite, list):
    with open('C:\Python34\items.csv', readwrite, newline='') as csvfile:

        if readwrite == 'r':
            useCSV = csv.reader(csvfile, delimiter=',')
            dataLines = [line for line in useCSV]
            return dataLines
        if readwrite == 'w':
            useCSV = csv.writer(csvfile, delimiter=',')
            useCSV.writerows(list)
            return