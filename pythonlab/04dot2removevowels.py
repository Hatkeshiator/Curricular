# Assignment 4, part 2
# Write a program to remove vowels from a string

reference = "AaEeIiOoUu"

def remove_vowels(string):
    for x in range(10):
        string = string.replace(reference[x],'')
    return string

def main():
    string = input("Enter your string: ")
    print(remove_vowels(string))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
