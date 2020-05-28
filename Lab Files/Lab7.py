"""
Lab 7 python file
"""
#
print("\n3.1")
current_number=-1
while current_number<6:
    current_number +=1
    if (current_number==3 or current_number==6):
        continue
    print(current_number)

#
print("\n3.2")
n=int(input("Enter a number:"))
factorial=1
while n>=1:
        factorial=factorial*n
        n=n-1
print(factorial)
#
print("\n3.3")
n=5
sum=0
total_numbers=n
while n>=0:
    sum=sum+n
    n=n-1
print(sum)
#
print("\n3.4")
x=3
product=1
while x in range(3,9):
    product=product*x
    x=x+1
print(product)
#
print("\n3.5")
x=1
product=1
while x in range(1,9):
    product=product*x
    x=x+1
print(product)

y=1
divisor=1
while y in range(1,4):
    divisor=divisor*y
    y=y+1
print(divisor)

final_answer=(product/divisor)
print(final_answer)
#
print("\n3.6")
num_list=[12,32,43,35]
print(num_list)
while num_list:
    num_list.pop(0)
    print(num_list)

"""
    num_list.remove(12)
print(num_list)
while 32 in num_list:
    num_list.remove(32)
print(num_list)
while 43 in num_list:
    num_list.remove(43)
print(num_list)
while 35 in num_list:
    num_list.remove(35)
print(num_list)
"""