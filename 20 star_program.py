a = int(input("enter the no. :" ))
l = a
m =a
for i in range(0,a+1):
    for k in range(0,l):
            print(end=" ")
    for j in range(0,i):
        print(end="*")
    print("")
    l = l-1
l=0
for i in range(0,a):
    for k in range(0,l):
            print(end=" ")
    for j in range(0,a):
        print(end="*")
    a= a-1
    print("")
    l = l+1






for i in range(0,m+1):
    for j in range(0,i):
        print(end="*")
    print("")

for i in range(0,m):
    for j in range(0,m):
        print(end="*")
    m= m-1
    print("")



