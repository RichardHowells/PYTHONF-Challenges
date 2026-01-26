# Lab05B

import os

# We use relative paths in this code.  
# Before getting going let's just confirm the current working directory 
print(os.getcwd())

print("All lines in the file\n")

# Old style. open and manual close
file = open(r".\employees.txt")
for line in file:
    print(line.strip())

file.close()

print("\nJust the unique ones\n")
# Display only unique items

# Modern style. with automates the close
with open(r".\employees.txt") as file:

    import pathlib 
    my_file = pathlib.Path(r".\unique_employees.txt")
    if my_file.is_file():
        print("I am about to nuke your file")


    with open(r".\unique_employees.txt", "w") as output_file:
        emp_nos = set()
        for line in file:
            if not line in emp_nos:
                emp_nos.add(line)
                print(line.strip())
                output_file.write(line)


# Demonstrate picking up values from the command line
# Such values can be used as file names, switches, etc
# (and it's probably best to use a library to handle them)

import sys
print(sys.argv)