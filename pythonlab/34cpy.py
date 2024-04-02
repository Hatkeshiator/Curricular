# Write a program to copy one file into another using file handling methods

def copy_file(a, b = "copy.txt"):
    # a is a string representing the path to the source file
    with open(a, 'r') as src:
        with open(b, 'w') as tgt:
            tgt.write(src.read())

    return True

a = input("Write complete path to the file you want to copy ")

copy_file(a)

with open('copy.txt', 'r') as file:
    print(file.read())

print("done")
