import csv

'''
# And this file just needs a little bit of configuration. This fucntion needs to write all info into .csv file that 
later can be opened in csv file
'''


def export_data(rows, filename):
    with open(filename, "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)


def read(filename, array):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            array.append(row)


def get_row(filename, row):
    data = []
    read(filename, data)
    return data[row]
