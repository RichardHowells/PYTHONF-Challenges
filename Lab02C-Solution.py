print("Q1")
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))




print("Q2")
list1 = [1, 2, 3, 4, 5, 6]

list2 = [4, 5, 6, 7, 8]

list2_missing = []

for i in list1:
    if i not in list2:
        list2_missing.append(i)

print("list2 missing values", list2_missing)

list2_additional = []

for i in list2:
    if i not in list1:
        list2_additional.append(i)

print("List2 additionals", list2_additional)

# The code would be very similar to determine missing values in list1 and additional values in list1


# The builtin set class has inbuilt logic for this kind of work
# with fewer lines of code
# Notice that although we get the same result VALUES, the actual result is a set
# You can tell because print() will show the curly braces 

print("List2 missing values (using set.difference)", set(list1).difference(set(list2)))
print("List2 additional values (using set.difference)", set(list2).difference(set(list1)))



print("Q3")
ls1 = [1, 5, 10, 20, 40, 80]

ls2 = [6, 7, 20, 80, 100]

ls3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("Common items are", set(ls1).intersection(set(ls2)).intersection(set(ls3)))



