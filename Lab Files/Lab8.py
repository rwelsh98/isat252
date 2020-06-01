"""
Lab 8 python file.
"""

print("\n3.1")

def cal_words(input_str):
    return(len(input_str.split()))

print("\n3.2")
demo_str="Hello world!"
print(cal_words(demo_str))

print("\n3.3")
def minimal_number(number_list):
    min_item=number_list[0]
    for number in number_list:
        if type(number) is not str:
            if min_item>=number:
                min_item=number
    return min_item
    

print("\n3.4")
demo_list=[1,2,3,4,5,6]
print(minimal_number(demo_list))

print("\n3.5")
mix_list=[1,2,3,4,'a',5,6]
print(minimal_number(mix_list))



