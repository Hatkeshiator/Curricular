# Assignment 20
# Write a program to sum over the elements in a list

def Sigma(l):
    mysum = 0
    for x in l:
        mysum += x
    return mysum

def main():
    mylist = input("Enter a list of space separated integers: ").split()
    mylist = [int(i) for i in mylist]
    print(Sigma(mylist))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")