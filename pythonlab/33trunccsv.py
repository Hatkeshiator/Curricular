# Write a program to read only columns with specific headers from a csv files

import csv

columns_to_read = input("What are the headings of the columns you want to read? ").split()

def readspecific(colslist):
    with open("myfile.csv", newline = '') as mycsv:
        robj = csv.DictReader(mycsv)
        for r in robj:
            truncrow = []
            for col in colslist:
                truncrow.append(r[col])
            for x in truncrow:
                print(f"{x}", end = ';\t')
            print("\n")
    return

readspecific(columns_to_read)
