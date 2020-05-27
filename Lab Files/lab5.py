"""
lab5 python file
"""

#3.1
alien_color='green'
if alien_color == 'green':
    print("You earned 5 points!")

#3.2
if alien_color is 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
    
#3.3
favorite_fruits=['mango','peach','pineapple']
if 'mango' in favorite_fruits:
    print("Mangos go great on sitcky rice.")
if 'apple' in favorite_fruits:
    print("Apples are okay.")
if 'pineapple' in favorite_fruits:
    print("I put salt on my pineapple to neutralize the acidity.")
if 'peach' in favorite_fruits:
    print("Peaches are juicy.")
if 'lemon'in favorite_fruits:
    print("I only like lemon in my water.")

#3.4
age=21
if age<10:
    print("You are a kid.")
elif 10<age<20:
    print("You are a teenager.")
elif age>=20:
    if age>=65:
        print("You are an elder.")
    print("You are an adult.")