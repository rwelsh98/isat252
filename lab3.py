"""
lab 3
"""
#3.1
str_list=["a","d","e","b","c"]
str_list.sort()
print(str_list)

#3.2
str_list.append("f")
print(str_list)

#3.3
str_list.remove("d")
print(str_list)

#3.4
print(str_list[2])

#3.5
my_list=['a','123',123,'b','B','False',False,123,None,'None']
my_unique_list=set(my_list)
print(len((my_unique_list)))


#3.6
message="This is my third python lab."
print(len(message.split()))

#3.7
num_list=[12,13,43,35]
num_list.sort()
print(num_list[-1],num_list[0])
# printing max and min value of a list

#3.8
game_board=[[0,0,0],[0,0,0],[0,0,0]]
print(game_board)

game_board[1]=[0,1,0]
print(game_board)