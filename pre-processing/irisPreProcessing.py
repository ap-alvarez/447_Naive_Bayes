# Matthew Wintersteen
# Iris Data Pre-processing
# 2019-09-05
# CSCI 447

import csv

def readCsv(file):
    lines = csv.reader(open(file, "r"))
    data = list(lines)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j] == 'Iris-setosa'):
                data[i][j] = '1'
            elif(data[i][j] == 'Iris-versicolor'):
                data[i][j] = '2'
            elif(data[i][j] == 'Iris-virginica'):
                data[i][j] = '3'
        data[i] = [float(x) for x in data[i]]
    return data

def writeCsv(file, data):
    with open(file, mode='w') as out:
        writer = csv.writer(out, delimiter=',')
        
        for x in data:
            writer.writerow(x)

def main():
    print("Iris Data Pre-Processing")
    # Read CSV file
    in_file = "../data/iris.data.csv"
    out_file = "../data/iris-preprocessed.csv"
    data = readCsv(in_file)
    print("Data has been read from the file {0} and pre-processed".format(in_file))

    # Write CSV file
    writeCsv(out_file, data)
    print("Data has been written to the file {0}".format(out_file))
    
main()


