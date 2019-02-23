#operator overloading

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return('A is (%d,%d)'%(self.a,self.b))

    def __add__(self,other):
        return (A(self.a + other.a,self.b + other.b))


a1 = A(12,8)
a2 = A(9,7)
print(a1+a2)
