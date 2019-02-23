# ,list

li = [1,2,3,4,5,6,7,8]

print(li)

#first element

print(li[0])
# last
print(li[-1])

#add some no.
li.append(150)
print(li)

#update

li[0] = 500
print(li)

# pop
li.pop()
print(li)
#delete item from list

del li[4]
print(li)

#remove

li.remove(3)
li.remove(8)
print(li)

#length
 
print(len(li))