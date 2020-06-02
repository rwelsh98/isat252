"""
Lab 9 python file
"""
print("\n3.1")
class My_stat:
    """An attempt to solve four equations with one large class."""
        
    def sigma(self,m,n):
        """Runs the sigma function in correspondence with lab 9."""
        self.result_sigma=0
        for i in range(n,m+1):
            self.result_sigma=self.result_sigma+i
            
        return self.result_sigma
        
    def pi(self,m,n):
        """Runs the pi function in correspondence with lab 9."""
        self.result_pi=1
        for i in range(n,m+1):
            self.result_pi=self.result_pi*i
        
        return self.result_pi    
   
    def factorial(self,m):
        """Runs a factorial function."""
        if m==0:
            return 1
        else:
            return m*self.factorial(m-1)
   
    def permutation(self,m,n):
        """Runs a permutation in correspondence with lab 9."""
        return self.factorial(m)/self.factorial(m-n)
        

print("\n3.2")
my_sigma=My_stat()
print(my_sigma.sigma(5,3))


my_pi=My_stat()
print(my_pi.pi(5,3))

my_factorial=My_stat()
print(my_factorial.factorial(5))

my_permutation=My_stat()
print(my_permutation.permutation(5,3))

