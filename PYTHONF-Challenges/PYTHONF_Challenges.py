
# Day 1




rate_per_widget = 0.50
quantity_made = 50

### Repeat for the 50 quantity

quantity_made = 50

pay = 0.50 * quantity_made
higher_rate_pay = 0
if quantity_made > 35:
    higher_rate_pay = (quantity_made - 35) * 0.50 * 0.50
    print('higher rate', higher_rate_pay)

pay = pay + higher_rate_pay

print('before bonus', pay)
if quantity_made > 45:
    pay = pay * 1.10

print('The pay for 50 is', pay)



# Lab02B

l = [10, 20, 30, 40]

# Mutate the list by adding these values, one at a time **in the order specified**, print 
# the state of the list after each modification.  Carefully consider using `.append` or `.insert` so that at the end the list is in ascending numerical order

l.append(45)
l.append(46)
l.insert(4, 44)
l.insert(4, 43)
l.insert(1, 15)
l.insert(3, 25)

print(l)

# Print all the even subscript items
print('even', l[0::2])
# Print all the odd subscript items
print('odd', l[1::2])

# Print the list in reverse order
l.reverse()     # Watch out. The reverse function actually changes the original list
print(l)

# Or... WATCH OUT HERE.  Reverse has ALREADY reversed the list.  So print(l[::-1]) prints it reversed a second time
# back into the original order 
print(l[::-1])

# The list l is still in reverse order.
  
l[0] = 5    # Content is now 5, 45, 44, etc
print(l)

