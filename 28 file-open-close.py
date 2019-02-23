# file is open and close

#open function

fo = open("foo.txt","w")
fo.write("welcome\n")
fo.write("hello sem\n")
fo.write("How are you bro?")

print("name of the file : ",fo.name)
print("closed or not : ",fo.closed)
print("opening mode : ",fo.mode)



#close

fo.close()
#check file open or closed

print("after close then check it out file closed or not : ",fo.closed)




