"""
Your module description
"""
def my_function(a,b):
    result=a+b
    return result
print(my_function(1,2))

#Arguments & Paramaters
def my_function(a,b):
    result=a+b
    
    print('a is ',a)
    print('b is',b)
    return result
print(my_function(1,2))

def my_function(a,b):
    result=a+b
    
    print('a is ',a)
    print('b is',b)
    return result
print(my_function(b=2, a=1))

def my_function(a,b=0):
    result=a+b
    
    print('a is ',a)
    print('b is',b)
    return result
print(my_function(1,2))

def my_function(a,b=0):
    
    print('a is ',a)
    print('b is',b)
    return a+b
print(my_function(a=1))

#Example 1
def calculate_abs(a):
    if a >0:
        return a
    if a<0:
        return -a
print(calculate_abs(-1))

#Example 2
result=0
for i in range(3,6):
    result=result+i
    
print(result)

result=0
for i in range(2,8):
    result=result+i

print(result)

def cal_sigma(m,n):
    result=0
    for i in range(n,m+1):
        result=result+i
    return result
print (cal_sigma(5,3))

def cal_pi(m,n):
    result=1
    for i in range(n,m+1):
        result=result*i
        
    return result
print(cal_pi(5,3))

 #Exercise 3- recursive function
def calc_factorial(m):
    if m==0:
        return 1
    else:
        return m+calc_factorial(m-1)
print(calc_factorial(0))

def calc_p(m,n):
    return calc_factorial(m)/calc_factorial(m-n)
print(calc_p(5,3))        
     