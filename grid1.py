space1 = 'X'
space2 = 'X'
space3 = 'X'
space4 = 'X'
space5 = 'X'
space6 = ' '
space7 = 'O'
space8 = ' '
space9 = ' '
print('   |   |   ')
print(' {} | {} | {} '.format(space1,space2,space3))
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' {} | {} | {} '.format(space4,space5,space6))
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' {} | {} | {} '.format(space7,space8,space9))
print('   |   |   ')
#toplinewinning
if (space1 == space2) and (space1 == space3):
    print('WIN')

    age = 15
if age < 18:
    print("Your age is {}.Child ticket is £8".format(age))
elif age > 18 and age < 60 :
    print("Your age is {}.Adut ticket is £10.95".format(age))
else:
    print("Your age is {}. Senior ticket is £7.50".format(age))



def coffee_order(size, drink_type):
    print("I would like to order a {}{} please".format(size, drink_type))

coffee_order("tall" , "Mocha")


def multiply_by_nine_fifths(celsius):
 return celsius * (9/5)
def get_fahrenheit(celsius):
 return multiply_by_nine_fifths(celsius) + 32

print("The temperature is {}°F".format(get_fahrenheit(15)))


def take_order(topping1, topping2):
    print("Pizza with {} and {} please".format(topping1, topping2))

take_order("pineapple" , "cheese")

#example
def cash_withdrawal(amount, accnum):
    print("Withdrawing {} from account {}".format(amount, accnum))

cash_withdrawal(300, 50449921)
cash_withdrawal(30, 50449921)
cash_withdrawal(200, 50447921)

balance = 4000
correctpin = 2222 
def check(pin, amount):
    if pin == correctpin and amount <= balance:
        print("dispensing cash - £" + str(amount))
    elif balance < amount:
        print("Not enough funds")
    else:
        print("incorrect pin")
def dispense_cash(pin, amount):
    check(pin, amount)
    if pin == correctpin and amount <= balance:
        print("You're new balance is £" + str(balance - amount))
dispense_cash(2222, 5000)

def multiply(num1, num2):
    return num1 * num2
print(multiply(3,8))

coffee_order = [
    "Sam - Hot Chocolate"
    "Andrew - Flat White"
    "Ezra - Champagne"
]
print(coffee_order)



fav_website = [
    "Youtube",
    "Kissanime",
    "Pinterest",
]
fav_website.append("Tumblr")
print(fav_website)

print("commit die options")
death_options = [
    "shooting myself",
    "drowning",
    "fall off a skyscraper"
]
death_options.append("consume too much chocolate")
print(death_options)