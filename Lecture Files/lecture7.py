"""
lecture 7 python file
"""

i=5
while i>=0:
    print(i)
    i=i-1
    
i=5
while i>=0:
    i=i-1
    if i==3:
        break
    print(i)

for word in 'hello world'.split():
    print (word)
    
    for str_item in word:
        
        if str_item=='l':
            break
        print(str_item)

while i>=0:
    i=i-1
    if i==3:
        continue
    print(i)
    
try:
    print(1/0)
except: #captures all errors, vs except()
    print('error')

try:
    print(1/0)
except ZeroDivisionError:
    print('Division by zero.')
    
i=5 
while i>=0:
    try:
        print(1/i-3)
    except:
        pass #break, pass, or continue? pass is the best.
    i=i-1
