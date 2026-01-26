# Lab04A

print("Q1")

def Add(x, y):
    return x + y

print("2 plus 2 =", Add(2,2))
print("9 plus -3 =", Add(9, -3))


print("Q2")

def calculate_pay(rate_per_widget, quantity_made):

    pay = rate_per_widget * quantity_made
    higher_rate_pay = 0
    if quantity_made > 35:
        higher_rate_pay = (quantity_made - 35) * 0.50 * 0.50
        print('higher rate', higher_rate_pay)

    pay = pay + higher_rate_pay

    print('before bonus', pay)
    if quantity_made > 45:
        over_45_bonus_rate = 1.1
        pay = pay * over_45_bonus_rate

    return pay

print("The pay for 30 units is ", calculate_pay(.50, 30))
print("The pay for 40 units is ", calculate_pay(.50, 40))
print("The pay for 50 units is ", calculate_pay(.50, 50))


# Bonus steps version...
def calculate_pay2(rate_per_widget, quantity_made, enhanced_pay_threshold1 = 35, enhanced_pay_threshold2 = 35):

    pay = rate_per_widget * quantity_made
    higher_rate_pay = 0
    if quantity_made > enhanced_pay_threshold1:
        higher_rate_pay = (quantity_made - enhanced_pay_threshold1) * 0.50 * 0.50
        print('higher rate', higher_rate_pay)

    pay = pay + higher_rate_pay

    print('before bonus', pay)
    if quantity_made > enhanced_pay_threshold2:
        over_45_bonus_rate = 1.1
        pay = pay * over_45_bonus_rate

    return pay

print("The pay for 30 units is ", calculate_pay2(.50, 30))
print("The pay for 40 units is ", calculate_pay2(.50, 40))
print("The pay for 50 units is ", calculate_pay2(.50, 50))



print("Q3")

def powers(n):
    '''
    Docstring for powers.  Powers takes a number and returns 
    it, the square, the cube, and the fourth power as a tuple
    
    :param n: Description
    '''
    return (n, n**2, n**3, n**4)

print(powers(2))
print(powers(3))
