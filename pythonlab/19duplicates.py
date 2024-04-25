# Assignment 19
# Write a program that counts the number of duplicate elements in a list.

# adds one to duplicate count for every occurence of an element that is not the first
def duplicount(l):
    duplicates = 0
    for i in range(len(l)):
        if l[i] in l[:i]:
            duplicates += 1
    print ("there are", duplicates, "duplicate items")


# adds one to duplicate count only if it is the second occurrence of that element
def Duplicount(l):
    duplicates = []
    for i in range(len(l)):
        if l[i] in l[:i] and l[i] not in duplicates:
            duplicates.append(l[i])
    print ("there are", len(duplicates), "duplicate items (", duplicates, ")")

# simply counts every non-unique element
def dupli_count(l):
    duplicates = 0
    for i in range(len(l)):
        l2 = l[:i] + l[i+1:]
        if l[i] in l2:
            duplicates += 1
    print ("there are", duplicates, "duplicate items")

def main():
    mylist = input("Enter a list of space separated integers: ").split()
    mylist = [int(i) for i in mylist]
    print(duplicount(mylist), Duplicount(mylist), dupli_count(mylist))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\nUses three functions which each have subtly different functionality, hence the three outputs.")
