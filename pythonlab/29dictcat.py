# Write a program that concatenates the dictionaries {1:10,2:20} {3:30,4:40} {5:50,6:60} to create a new dictionary

def concat_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

result = concat_dicts(dict1, dict2)
result = concat_dicts(result, dict3)

print(result) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
