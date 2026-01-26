rate_per_widget = 0.50
quantity_made = 30

### Calculate the pay here

pay = rate_per_widget * quantity_made
print(pay)

quantity_made = 40

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet
pay = rate_per_widget * quantity_made

print(pay)

### Repeat for the 50 quantity
quantity_made = 50

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet
pay = rate_per_widget * quantity_made

print(pay)

### For widgets over 35 bonus...

quantity_made = 45
if quantity_made > 35:
    excess_widgets = quantity_made - 35
else:
    excess_widgets = 0

basic_pay = rate_per_widget * quantity_made
higher_rate_pay = excess_widgets * 0.5 *rate_per_widget

pay = basic_pay + higher_rate_pay
print(pay)

### For widgets over 45 bonus

quantity_made = 50
if quantity_made > 35:
    excess_widgets = quantity_made - 35
else:
    excess_widgets = 0

basic_pay = rate_per_widget * quantity_made
higher_rate_pay = excess_widgets * 0.5 *rate_per_widget

pay = basic_pay + higher_rate_pay

if quantity_made > 45:
    pay = pay * 1.1

print(pay)


### Working with strings

mixed = "MiXed CasE"

upper = "UPPER CASE"

lower = "lower case"

print(upper.isupper(), lower.isupper(), mixed.isupper())
print(upper.islower(), lower.islower(), mixed.islower())

print(upper.upper(), lower.upper(), mixed.upper())
print(upper.lower(), lower.lower(), mixed.lower())

answer = input("Should I format your hard disk? (y/n)")
if answer.upper() == 'YES':
	print('Formatting...')
	# Code to format HDD goes here
else:
	print('I am sad - I really wanted to format your disk!')
