#Exception

try:
    fo = open("sem",'r')# sem file to be read
except IOError:
    print("this is can't find file this name")
else:
    print("I thing it happen what u want?")
