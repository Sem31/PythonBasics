# dictionary method


dict1 = {'name':'sem','roll':47,'adderss':'155'}
print(dict1)

#shallow copy

dict2 = {'sub':['c','c++','java']}
dict2['sub'].append('maths')
print(dict2)
dict2 = dict1.copy()
print("new : ",dict2)

#fromkeys method

seq = ('age','name','party')
dict2 = dict2.fromkeys(seq)
print(dict1)
dict2 = dict2.fromkeys(seq,10)
print(dict2)

#get

print("get name : ",dict1.get('name'))
print("get name : ",dict2.get('age'))

#item method
print(dict1.items())

#clear method
dict1.clear()
print("clear : ",len(dict1))



