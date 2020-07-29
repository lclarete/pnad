import csv
import io

TOTAL_LINES = 362556


def read_file(path):
    with io.open(path, encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(readCSV):
            print(index, row)


if __name__ == '__name__':
    read_file('PES2013.sample.csv')
