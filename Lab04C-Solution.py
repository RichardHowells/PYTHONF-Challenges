# Lab04C

def range_checker(n):
    if n < 0 or n > 100:
        raise ValueError()
    

try:
    range_checker(10)
except ValueError:
    print("The value was outside the allowed range")
else:
    print("The value is in range - continuing")

print("Normal code continuing")

try:
    range_checker(-1)
except ValueError:
    print("The value was outside the allowed range")
else:
    print("The value is in range - continuing")
    
# Notice that this next line is executed, despite the exception
# because the except clause handles the exception
print("Normal code continuing")

