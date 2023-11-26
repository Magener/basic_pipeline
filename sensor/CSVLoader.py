import csv


def generator_from_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            yield row