def fact(n):
    k=1
    for i in range(1,n+1):
        k = k*i 
    return k


n = 5
l = fact(n)
print(l)



def student(listof):
    for s in listof:
        print(s)
        
li = ["sem","kamlesh","vishal","baba"]
student(li)