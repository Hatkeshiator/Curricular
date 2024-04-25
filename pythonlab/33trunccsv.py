# Assignment 33
# Write a program to read only columns with specific headers from a csv files

import csv

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

def main():
    columns_to_read = input("What are the headings of the columns you want to read? ").split()
    readspecific(columns_to_read)

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()