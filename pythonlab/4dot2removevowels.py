# Write a program to remove vowels from a string

reference = "AaEeIiOoUu"

def remove_vowels(string):
    for x in range(10):
        string = string.replace(reference[x],'')
    return string

string = input("Enter your string: ")
print(remove_vowels(string))
