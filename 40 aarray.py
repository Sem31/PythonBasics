from array import *
a = []
n = int(input("no of array : "))
for i in range(0,n):
    no = int(input("no of array : "))
    a.append(int(no))

    
for i in range(0,n):
    print(a[i])


for j in range(0,n):
    i = 0
    while i<n-1:
        if a[i]<a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        i = i+1

for i in range(0,n):
    print(a[i])




