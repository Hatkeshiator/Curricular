ref = "AEIOUaeiou"
def counter(string):
    count = 0
    for char in string:
        if char in ref:
            count += 1
    return count

a = input("Enter your string: ")
print(counter(a))
