import csv
from os import path

file_path = input("Enter The file path: ")

active = True

while active:
    if path.exists(file_path) and file_path.endswith('csv'):
        print('File will be ready @ BatmonLogCleaned.csv in root folder')

        with open(file_path, 'r+') as inp, open('BatmonLogCleaned.csv', 'w+') as out:
            cleaned_file = csv.writer(out)

            input_file = csv.reader(inp)
            next(input_file)

            row_starter = "Day"

            headerCount = 0

            for row in input_file:

                if row[0] == row_starter and headerCount == 0:
                    headerCount += 1
                    cleaned_file.writerow(row)

                if row[0] != row_starter and headerCount >= 1:
                    cleaned_file.writerow(row)
        break

    else:
        print('File does not exist or invalid file type exiting program')
        active = False

