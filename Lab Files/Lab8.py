"""
Lab 8 python file.
"""

print("\n3.1")

"""
def words_str():
     x=len(message.split())
     print("This string has ",x," number of words in it.")
words_str()
"""

print("\n3.2")
def words_str():
    x=len(message.split())
    print("This string has ",x," words in it.")
    
message=demo_str='Hello world!'
print(message)
words_str()

"""
print("\n3.3")
def minimal_numbers():
    for x in x_list:
        y=min(x_list)
        print(min(x_list))

print("\n3.4")
x_list=demo_list=[1,2,3,4,5,6]
"""
print("\n3.5")
mix_list=[1,2,3,4,'a',5,6]
min_item=mix_list[0]

def minimal_numbers(x_list):
    mix_list=[1,2,3,4,'a',5,6]
    min_item=mix_list[0]
    for number in x_list:
        if min_item>=number:
            min_item=number
        print("The minimum number in this list is,",min_item,".")
minimal_numbers(x_list=mix_list)




