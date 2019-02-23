#basic operaor of list

list1 = [1,2,3,4,5,6]
list2 = [8,9,7,'s']

print("list1 =  ",list1,"list2 =  ",list2)

list3 = list1+list2
print("concatination = ",list3)
list4 = list2*2
print("repitation = ",list4)
list5 = len(list1)
print("length list1 is = ",list5)
print("slice from 2 = ",list2[2:])

print("negative slicing from -2 = ",list2[-2:])


#delete

del list1[3]
print("deleted list1 element 3 is ",list1)

del list2
print(list2)

