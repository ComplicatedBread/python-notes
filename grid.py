name = "Catriona"

Age = 19

Favourite_colour = "Red"

print("My name is {}".format(name))

print("I am {}".format(Age))

print("My favourite colour is {}".format(Favourite_colour))

#2nd task

Breakfast = "Cheerios"

Lunch = "Chips"

Dinner = "Steak"

print("For breakfast I had {}".format(Breakfast))

print("For lunch I had {}".format(Lunch))

print("For dinner I will have {}".format(Dinner))

#3rd task

from datetime import date
age = date.today()-date(2000,8,22)
print(age.days)
days= (age.days)
years= days / 365
print("number of years is: ");
print(years);

from datetime import date
today = date.today()
print(today)

my_bday = date(2000,8,22)
print(today)
print ((today - my_bday).days)
