# PYTHONF-Challenges

# Day 1
# Calculating Pay

Jemima take a job making widgets.  She is paid 50p for each widget she makes.

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
little research for this, as of Day 1 we have not properly covered the `if` statement.  Don't worry if you have trouble with this we will
cover the `if` statement properly later on

Test it as above

Extend it again so that after Jemima produces 45 widgets she gets a 10% bonus on her entire pay

Test it as above

# Day 2
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
```

The loop will set the variable `quantity_made` one by one to the members of the list.  Inside teh body of the loop it prints that value.  Run it to make sure
it displays the three quantity values

Copy/paste ONE copy of the pay calculation code into the loop body.  It must be indented to become the loop body

REMOVE the assignment to `quantity_made`, the loop already does that.

Test to see that the loop produces the same results as the original repeated code

Add some more test values to the list




# Day 3
# Counting characters

