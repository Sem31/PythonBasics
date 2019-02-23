#globals and locals function

#globals

count =2000

def add():
    global count
    count = count+1

print(count)
add()
print(count)
