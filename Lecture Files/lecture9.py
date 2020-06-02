"""
Lecture 9 python file
"""
class Car:
    
    maker='toyota'
    
    def report_maker(self): #method
        return(self.maker)
        
my_car=Car()
print(my_car.maker)
print(my_car.report_maker())

""" """
class Car:
    
    maker='toyota'
    
    def __init__(self, input_model):
        self.model=input_model

my_corolla=Car('corolla')
print(my_corolla.maker)
print(my_corolla.model)

my_highlander=Car('highlander')
print(my_highlander.maker)
print(my_highlander.model)

""" """
class Car:
    
    maker='toyota'
    
    def __init__(self, input_model):
        self.model=input_model
        
    def report(self):
        #return the attribute of the instance
        return self.maker,self.model
        
my_corolla=Car('corolla')
print(my_corolla.report())

my_car=Car('corolla')
print(my_car.report())

my_car.maker='ford'
print(my_car.report())    
    