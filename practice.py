list1 = [1,2,4,5,7,3,8]

print("list : ",list1)

print("membership func :  ",5 in list1)
print("membership func :  ",51 in list1)
print("membership func :  ",51 not in list1)

list1[2] = 101

print("update : ",list1)

list1.remove(2)
print("remove : ",list1)

print("max : ",max(list1))
print("min : ",min(list1))
list1.append(150)
print("append : ",list1)

print("lenght : ",len(list1))

list2 = ['s','e','m']

print("concatenation : ",list1+list2)
print("repetation : ",list2*2)
list1.reverse()
print("reverse : ",list1)
list1.sort()
print("sort : ",list1)


list3 = list1
print("copy : ",list3)

list1.extend('sem')
print("extend : ",list1)


a = int(input("enter the no. ="))
b = int(input("enter the second no. = "))
c = int(input("enter the third no. = "))

if a>b and a>c:
    print("a is big")
elif b>a and b>c:
    print("b is big")
else:
    print("c is big")

i = 1
while i>a :
    print(i, end=" ")
    i = i+1
else:
    print("false")



for i in range(1,11):
    k = i*b
    print(k, end=" ")
    i = i+1

for i in "sem":
    print(" ",i)
    
    

