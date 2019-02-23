# list methods

#append
list1 = [1,2,3,4]
list1.append(5)
print(" ",list1)

#count

list1 = ['k',1,3,1,1,1,'k']

print("count k is ",list1," : ",list1.count('k'))
print("count 1 is ",list1," : ",list1.count(1))

#extend

list1 = ['S','E','M','P']
list2 = list(range(5))
list1.extend(list2)
print("extende list is : ",list1)

#index

list = ['S','e','m']
print("e is in index of = :",list.index('e'))


#reverse
list = ['S','e','m']
list.reverse()
print("reverse of the list  is : ",list)

#sort

list1 = [5,4,3,2,1]
list1.sort()
print("sort is = ",list1)
