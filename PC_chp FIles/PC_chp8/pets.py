"""
Arguments
"""
#Positional Argument
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

describe_pet('dog','willie')

#Keyword Argument
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='harry')

#default values
def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='willie')

describe_pet(pet_name='harry',animal_type='hamster')