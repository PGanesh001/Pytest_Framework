import pandas

def read_csvfile(file_path):
    csvFile = pandas.read_csv(file_path)
    return csvFile

