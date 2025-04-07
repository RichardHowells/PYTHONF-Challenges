# PYTHONF-Challenges

# Day 1
# Calculating Pay

Jemima takes a job making widgets.  She is paid 50p for each widget she makes.

Write a program to calculate her pay for making 30 widgets, 40 widgets and 50 widgets.

You should use variables here.  It will make later parts of this challenge **much** easier.  Start with somthing like:

```
rate_per_widget = 0.50
quantity_made = 30

### Calculate the pay here

print(pay)

quantity_made = 40

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet

print(pay)

### Repeat for the 50 quantity
```


Manually calculate the expected values and test that the program produces the results you expect

Extend that program so that for each widget after 35 Jemima is paid at a 50% higher rate per widget. You will have to do a 
little research on the `if` statement for this.  As of Day 1 we have not properly covered the `if` statement.  Don't worry if you have trouble with it we will
cover the `if` statement properly later on

Test it as above

Extend your code again so that after Jemima produces 45 widgets she gets a 10% bonus on her entire pay

Test it as above


# Working with string methods...

Set up a string with mixed case text in it, a string that's all upper case, and a string thats all lower case.

In the python docs look up the string methods. 

Experiment with isupper(), islower() do they correctly report your strings?

Experiment with lower and upper.

These are often useful with user input.  For example, if we get the user to answer a question y for yes n for no.
We cannot predict whether they will type the letters in Lowercase or uppercase. A common programming technique is to 
convert what they enter 
into either all uppercase or all lowercase . This makes it easier for us to write conditions . Something like...

```
answer = input("Should I format your hard disk? (y/n)")
if answer.upper() == 'Y'
	print('Formatting...')
	# Code to format HDD goes here
else
	print('I am sad - I really wanted to format your disk!')
```

Experiment with that code.  Expand it to accept the full words (yes/no) as the response





# Day 2

# Lab02B

# Mutating a list...

Create a list containing the values 10, 20, 30, 40

Mutate the list by adding these values, one at a time **in the order specified**, print 
the state of the list after each modification.  Carefully consider using `.append` or `.insert` so that at the end the list is in ascending numerical order

45
46
44
43
15
25

Print all the even subscript items

Print all the odd subscript items

Print the list in reverse order






# Using a loop

We have not taught loops yet, but they go hand-in-hand with sequence type collections...

Working with the code challenge from day 1, set up a list, named `quantities` to contain the quantities of widgets Jemima makes - 30, 40, and 50

Paste in this code to iterate through those values...

```
for quantity_made in quantities:
	# Indented 
	# code 
	# for 
	# the 
	# loop 
	# body
	print(quantity_made)

# un-indented code does not belong to the loop
print('Loop ended')
```

The loop will set the variable `quantity_made` one by one to the members of the list.  Inside teh body of the loop it prints that value.  Run it to make sure
it displays the three quantity values

Copy/paste ONE copy of the pay calculation code into the loop body.  It must be indented to become the loop body
```
rate_per_widget = 0.50
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

```

REMOVE the assignment to `quantity_made` inside the loop body.  The loop header already does that.

Test to see that the loop produces the same results as the original repeated code

Add some more test values to the list.

**Question** Which are the best test values?  Why?





# Day 3
# Counting characters

