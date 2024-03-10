# Write a program to read two text files and merge their contents

def initialize_files():
    
    with open('17file1.txt', 'w') as file:
        file.write("Hello, ")
    
    with open('17file2.txt', 'w') as file:
        file.write("World!")
    
    return True

def merge_files():
    
    with open('17file1.txt', 'r') as file1:
        with open('17file2.txt', 'r') as file2:
            result = file1.read() + file2.read()
    
    with open('17cat.txt', 'w') as file:
        file.write(result)
    
    return True

initialize_files()
merge_files()