# Write a program to generate a CSV file that has one column containing each alphabet, and one column containing a random integer. The headings of these columns should be alphabet and count respectively.  Also plot a histogram over the alphabets that represents the count of each.

import csv

def tsri(seed):
    return [((x ** 5) + ((seed % 631) * x ** 4) + (seed * x ** 3) + (18 * x ** 2) + ((seed + 45) * x) + (seed)) % ((seed // 5) + 107) for x in range(26)]

def makecsv(seed):
    with open("alphabet.csv", 'w', newline='') as file:
        w = csv.writer(file)
        w.writerow(['alphabet','count'])
        nums = tsri(seed)
        chars = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(chars)):
            w.writerow([chars[i], nums[i]])
    return



import matplotlib.pyplot as plt

def plotgraph():
    letters = []
    counts = []
    with open('alphabet.csv', "r") as file:
        r = csv.reader(file)
        next(r)
        for row in r:
            letters.append(row[0])
            counts.append(int(row[1]))
    
    plt.bar(letters, counts)
    plt.title('Histogram of letters and their counts')
    plt.xlabel('Letter')
    plt.ylabel('Count')
    plt.grid(axis='y')
    plt.show()
