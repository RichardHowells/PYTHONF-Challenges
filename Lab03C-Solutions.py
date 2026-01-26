# Lab03C

print("Q1")

for n in range(101):
    if n > 9:
        break
    print(n)
else:
    print("Loop exited normally")


print("Q2")
sum = 0
for n in range(21):
    sum += n

print(sum)

print("Q3")

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
index = 0
for n in lst:
    if n == 100:
        print(100, "is at index", index)
    index += 1

# Alternative solution
index = 0
while index < len(lst):
    if lst[index] == 100:
        print(100, "is at index", index)
    index += 1

print("Q4")

sum = 0
num = int(input("Enter a number to sum.  Zero to calculate and display "))
while(num != 0):
    sum += num
    num = int(input("Enter a number to sum.  Zero to calculate and display "))

print("The sum is", sum)


print("Q5")

quantities = [30, 40, 50]

for quantity_made in quantities:
    rate_per_widget = 0.50

    pay = 0.50 * quantity_made
    higher_rate_pay = 0
    if quantity_made > 35:
        higher_rate_pay = (quantity_made - 35) * 0.50 * 0.50
        print('higher rate', higher_rate_pay)

    pay = pay + higher_rate_pay

    print('before bonus', pay)
    if quantity_made > 45:
        pay = pay * 1.10

    print(f'The pay for {quantity_made} is', pay)
## un-indented code does not belong to the loop
print('Loop ended')



print("Q6")

quantities = [30, 40, 50]

for quantity_made in quantities:
    rate_per_widget = 0.50

    pay = 0.50 * quantity_made
    higher_rate_pay = 0
    if quantity_made > 35:
        higher_rate_pay = (quantity_made - 35) * 0.50 * 0.50
        print('higher rate', higher_rate_pay)

    pay = pay + higher_rate_pay

    print('before bonus', pay)
    if quantity_made > 45:
        for over_45_bonus_rate in [1.1, 1.15, 1.2]:
            pay = pay * over_45_bonus_rate
            print(f"with over 45 bonus of {over_45_bonus_rate} pay is", pay)

    print(f'The pay for {quantity_made} is', pay)
## un-indented code does not belong to the loop
print('Loop ended')

