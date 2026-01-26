
print("Q1")

dictionary = {"Shanghai":17.8, "Istanbul":13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(dictionary)



print("Q2 - string, int, float")
# A list cannot be a key because keys must be immutable


print("Q3")

keys = ['key1', 'key2', 'key3']

values = [1, 2, 3]

# zip will take the first item in the keys sequence and 
# pair it with the first value in the values sequence
# Then the second tiem in each sequence...
pairs = zip(keys, values)

# The dict constructor will take each incoming pair (k, v)
# and load it into the dictionary with k as the key and v as the value
dictionary = dict(pairs)
print(dictionary)



print("Q4")
dict_1 = {'key1': 1, 'key2': 2, 'key3': 3}

dict_2 = {'key4': 4, 'key5': 5, 'key6': 6}

dict_1.update(dict_2)
print(dict_1)

# If dict_1 must not be unmodified then
dict_3 = dict(dict_1)  # Copy the dictionary, why is dict_3 = dict2 not going to work?
dict_3.update(dict_2)
print(dict_3)


print("Q5")
dictionary = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print(dictionary["class"]["student"]["marks"]["history"])