
a = []
n = int(input("ENter the array : "))

for i in range(0,n):
    k = int(input("ENter the array : "))
    a.append(int(k))

print("\n Your list is : ")
for i in range(0,n):
    print("array : ",a[i])


print("\nBubble sort :\n")

for j in range(0,n):
    for i in range(0,n-1):
       if a[i]>a[i+1]:
          a[i],a[i+1] = a[i+1],a[i]
    
for i in range(0,n):
    print("array : ",a[i])
