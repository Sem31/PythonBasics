
#code for write in the files

with open("C:/Users/hp/Desktop/python/kp.txt",'w') as obj:
    obj.write("Sem is here\n")
    obj.write("kesa ha bhai\n")    
    obj.write("kesa ha bhai\n")    
    obj.write("kesa ha bhai\n")    
    obj.write("kesa ha bhai\n")

# code for append in the file

with open("C:/Users/hp/Desktop/python/kp.txt",'a') as obj:
    obj.write("Sem is here 1\n")
    obj.write("kesa ha bhai 2\n")    
    obj.write("kesa ha bhai 3\n")    
    obj.write("kesa ha bhai 4\n")    
    obj.write("kesa ha bhai 5\n")

# read file code

with open("C:/Users/hp/Desktop/python/kp.txt",'r') as obj:
    data  = obj.read()
    print(data)