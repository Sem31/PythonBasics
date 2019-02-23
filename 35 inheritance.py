class Add:
    c = 0
    n = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        self.c = self.a + self.b
        return self.c
    def dis1(self):
        print("sum of is : ",self.c)


    def setattr(self,attr):
        self.n = attr
        print("called set attribute method of n")
    def getattr(self):
        print("get attribute of n is : ",self.n)



        

class multi(Add):
    k = 0
    def __init__(self,a,b):
        super().__init__(a,b)
        print("super will be called : ")

    def mul(self):
        self.k = self.a * self.b
        return self.k
    def dis(self):
        print("multi of is : ",self.k)



a,b = 12,13
m1 = multi(a,b)
m1.sum()
m1.dis1()
m1.mul()
m1.dis()

m1.setattr(150)
m1.getattr()

