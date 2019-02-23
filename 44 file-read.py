# Create file and read it 
f = open("k.txt",'w')
f.write("kamlesh\n")
f.write("Sem")
f = open("k.txt",'r')
print(f.read())

f.close()
