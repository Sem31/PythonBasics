# Exception progarm

a = int(input("Enter the value : "))
b = int(input("Enter the value : "))


try:
    c = a/b
    print("Division is : ",c)
except:
    print("Error.....Divisible by Zero error")
