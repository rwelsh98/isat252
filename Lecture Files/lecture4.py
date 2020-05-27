"""
lec 4, tuple and dictionary
"""
my_tuple='a','b','c','d','e'
print(my_tuple)

my_2nd_tuple=('a','b','c','d','e')
print(my_2nd_tuple)

test='a'
print(type(test)) #not a tuple bc no comma

Test='a',
print(type(Test))

print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])

my_car={
        'color':'red',
        'maker':'toyota',
        'year':2015
        }
print(my_car['year'])
print(my_car.get('year'))

my_car['model']='corolla'
print(my_car)

my_car['year']=2020
print(my_car)

print(len(my_car))
print('color'in my_car)
print('mile' in my_car)