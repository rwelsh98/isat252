"""
lecture 5 python note: Boolean,None(null), 
"""
print(1+2)
print(1+

        2)

print([1,2,3,
    
        4,5,6]  )

m=1+2
print(m)

m=1+\
    2
print(m)

a=123
print(a)
print(id(a))
print(id(123))

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
print(id(a))
print(id(b)) #false due to different id values

x= None
print(id(None))
print(id(x))
print(x is None)
print(x==None)

y=[]# list
print(type(y))

print(y==None)

print(True)
print(False)

print(True or False)
print(True and False)
print(not True)

print(not None)
print(not '0')
print(not 0)

print(() and [])

#flow control
if 2>1:
    print('2>1')
    
if 2<=1:
    print('2<=1')

if 2>1:
    if 1.5>1:
        print('1.5>1')
    print('2>1')
    
if 2>1:
    if 1.5<1:
        print('1.5<1')
    print('2>1')
    
if 2<=1:
    print('2<=1')
else:
    print('2>1')
    
#if-elif-else
if 2<=1:
    print('2<=1')
elif 2<=2:
    print('2<=2')
else:
    print('2>1')
    
if None:
    print(1)
elif {}:
    print(2)
elif '0':
    print(3)
else:
    print(4)