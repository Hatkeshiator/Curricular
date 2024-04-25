# Assignment 18
# Write a program to create a CSV file and write a table of USER-IDS and PASSWORDS to it.
# The program should then read a password from the user and print the corresponding USER-ID if applicable, else throw an appropriate error message.

def initialize_csv():
    # csv is a surprisingly simple format so we don't need to import csv because we're not lazy and write code ourselves.
    with open('18csv.csv', 'w', newline='') as file:
        file.write("User-ID,Password\n")
        file.write("user1,pass1\n")
        file.write("user2,pass2\n")
        file.write("user3,pass3\n")
    
    return True

def read_csv(p):
    # p is the password    
    with open('18csv.csv', 'r') as file:
        # iterating over a file goes line by line
        for line in file:
            if p + '\n' in line:
                result = line.split(',')[0]
                break
        else:
            result = "No user with that password"
    
    return result

def main():
    initialize_csv()
    password = input('Enter the password: ')
    print(read_csv(password))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
