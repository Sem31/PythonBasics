#Hiding of the data in python

class A:
    def __init__(self,x):
        self._c = x
        self.__cc = 10


a1 = A(5)
# access the Single underscore data simple
print("Single underscore : ",a1._c)

# access the double underscore data by using the class name otherwise they are not accesseble out side the class see on the next line of it

print("access the hide data on class : ",a1._A__cc)

#not access the data of class out side the class using double underscore 
print("double underscore data are not access directly : ",a1.__cc)
