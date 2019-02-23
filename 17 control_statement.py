# control statements in loops

#break

for i in range(1,11):
    print("i is less then 6 :",i)
    if i>6:
        print("i<6 is big one= ",i)
        break
    i = i+1
    
#continue

for i in range(1,11):
    if i>6:
        print("continue afer this one = ",i)
        continue
    i = i+1

