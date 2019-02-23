
#mrhtod overloading in python




def collect(a, b=None):
    if b==None:
        return a
    else:
        return a+b

print(collect(2))
print(collect(2,5))