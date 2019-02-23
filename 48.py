li = [1,2,63,9,7,8]
print(li)
#add item by append

li.append(9)
print(li)

#update the element

li[0] = 1554
print(li)

#slice
print(li[:3])
print(li[3:])
print(li[3:5])

#remove item
#delelte item
del li[0]
print(li)

li.remove(7)
print(li)

del li[:3]
print(li)