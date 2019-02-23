#inheritance

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("call A constructor")
    
    def add(self):
        print("sum is  : ",a+b)

class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)
        print("call multi constructor")
    
    def mult(self):
        print("multi : ",a*b)

a=13
b =15
m = B(a,b)
m.add()
m.mult()