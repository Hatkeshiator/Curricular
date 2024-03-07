# Write a program to create a CSV file and write a table of USER-IDS and PASSWORDS to it.
# The program should then read a password from the user and print the corresponding USER-ID if applicable, else throw an appropriate error message.

import csv

def write_csv():
    # Open the CSV file
    with open('17csv.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['User-ID', 'Password'])
        # Write the table
        writer.writerow(['user1', 'pass1'])
        writer.writerow(['user2', 'pass2'])
        writer.writerow(['user3', 'pass3'])
    # Close the file
    file.close()

def read_csv(p):
    # Open the CSV file
    with open('17csv.csv', 'r') as file:
        reader = csv.reader(file)
        # Read the table
        for row in reader:
            if row[1] == p:
                print('User-ID:', row[0])
                return
        print('No user with that password found')
    # Close the file
    file.close()

write_csv()
password = input('Enter the password: ')
read_csv(password)