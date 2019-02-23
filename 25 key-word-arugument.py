# keyword arugument

def detail(name,age):
    print("name : ",name)
    print("age : ",age)

    return
print("\tfirst data")
detail('sem',21)
print("\tSecond data")
detail('kamlesh',23)


#default arugument


def detail(name,age=50):# this age only for those there age should be default
    print("name : ",name)
    print("age : ",age)

    return
print("\tfirst data")
detail('sem')
print("\tSecond data")
detail(age =23,name ='kamlesh')  # autometically change according to def function


#variable length arugument

def variable(var,*vartuple):
    print("output is : ")
    print(var)


    for var in vartuple:
        print(var)
    return

variable(10)
variable(70,80,90,40) # this 80 to 40 are store in *vartuple in form of tuple  
    










