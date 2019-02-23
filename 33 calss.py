
# with init method

class fact:
    k = 1
    def __init__(self,n):
        self.n = n

    def factorial(self):
        for i in range(1,self.n+1):
           self.k = i*self.k

    def display(self):
        print("factorial is : ",self.k)

        


f1 = fact(5)
f1.factorial()
f1.display()


# without init method

class fact:
    k = 1
    
    def factorial(self,n):
        self.n = n
        for i in range(1,self.n+1):
           self.k = i*self.k

    def display(self):
        print("factorial is : ",self.k)

        


f1 = fact()
f1.factorial(6)
f1.display()


