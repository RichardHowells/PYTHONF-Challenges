# Functions module

print("Hello from functions.py")

def square(n):
    return n * n

def tupleExtender(t, newItem):
    tuple_as_list = list(t)
    tuple_as_list.append(newItem)
    return tuple(tuple_as_list)