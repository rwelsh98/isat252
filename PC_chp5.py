"""
Python Crash Course chapter 5
"""
#cars.py
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
        
#toppings.py
requested_toppings='mushrooms'
if requested_toppings !='anchovies':
    print("Hold the anchovies!")
#!= is equivalent to not equal

#magic_number.py
answer=17
if answer !=42:
    print("That is not the correct answer. Please try again!")

#banned_users.py
banned_users=['andrew', 'carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
#voting.py
age=19
if age>=18:
    print("You are old enough to vote!")

#if-else statements
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registereed to vote yet?")
else:
    print:("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
#if-elif-else Chain
#amusement park.py
"""
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    """
"""
age=12
if age<4:
    price=0
elif age<18:
    price=25
else:
    price:40
print(f"admission cost is ${price}.")
"""
"""
age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price40
else:
    price=20
print(f"Your admission cost is ${price}.") 
"""
"""
age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"admission cost is ${price}.")
"""
#toppings.py
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza.")