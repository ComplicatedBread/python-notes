time = 1800
place_of_work = "Highview"
town_of_home = "Ramsbottom"

if time == 700:
    print(town_of_home)
elif time == 900:
    print(place_of_work)
else:
    print("commuting")

password = "hi"

print (len(password))
if (len(password)) <8:
    print("Password is too short")
else:
    print(password)

num = 50
if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")


num = 89

if num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 and num % 5: #this goes first
    print("fizzbuzz")
else:
    print(num)

num1 = 1
num2 = 3
if (num1 + num2) % 2 ==0:
    print("success!")
else:
    print("")

#copied

    num = 1233321
num_string = str(num)
num_string_reversed = num_string[::-1]
if num_string == num_string_reversed:
    print('{} is a Palindrome'.format(num_string))
else:
    print('{} is a Not a Palindrome'.format(num_string))

def sandwich_order(top1, top2, top3, top4, top5):
    print("Preparing order with {}, {}, {}, {} and {}")



for i in range(5):
    print(i)

for i in range (9, -1, -1):
    print(i)

fave_films = ["Legend of the guardians", "The hobbits", "HTTYD", "Lord of the rings", "Harry Potter"]
for i in range(len(fave_films)):
    print(fave_films[i])


    fav_films = [
    "True Romance",
    "The Descent",
    "Ghost",
    "Aliens",
    "Scream"
]
​
fav_films.insert(4, "Scream 2")
fav_films.append("You're Next")
​
​
for film_index in fav_films:
    print(film_index)
​
def film_check():
    if fav_films[2] == "Ghostbusters":
        print("Yay, it is Ghostbusters.")
    else:
        print("Boo, we would prefer Ghostbusters.")
​
film_check()