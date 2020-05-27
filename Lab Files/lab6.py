"""
lab 6 python file
"""
#3.1
for x in range(6):
    if(x==3 or x==6):
        continue
    print(x)

#3.2
n=input("\nEnter a number:")
factorial=1
if int(n)>=1:
    for i in range (1,int(n)+1):
        factorial=factorial*i
print("Facotrial of ",n," is: ",factorial)

#3.3
n=input("Enter number to calculate the sum:")
n=int(n)
sum=0
for num in range(0,n+1,1):
    sum=sum+num
print("Sum of range is:", sum)
#or
result=0
for num in range (1,6):
    result=result+num
print(result)

#3.4
product=1
for each_num in range(3,9):
    product=product*each_num
print(product)

#3.5
product=1
for num in range(1,9):
    product=product*num
#print(product)
    
divisor=1
for number in range(1,4):
    divisor=divisor*number
#print(divisor)

final_answer=product/divisor
print(final_answer)

#3.6
count=0
for word in 'this is my 6th string'.split():
    count=count+1
    
print(count)
    
#3.7
count=0
my_tweet={
        "favorite_count":1138,
        "lang":"en",
        "coordinates":(-75,40),
        "entities":{"hashtags":["Preds","Pens","SingintoSpring"]}
            }
print(my_tweet['entities']['hashtags'])
result=0
for my_hashtag in my_tweet['entities']['hashtags']:
    result=result+1
print(result)