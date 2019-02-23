#overriding

class A:
    def __init__(self):
        print("parent class init method")
    def hello(self):
        print("parent class")
    def setattr(self,n):
        self.n = n
    def getattr(self):
        print("parent attribute value is : ",self.n)

class B(A):
    def __init__(self):
        super().__init__()
        print("base class init method..")
    def hello(self):
        print("overriding parent class")
        
b1 = B()
b1.setattr(100)
b1.getattr()

b1.hello()

