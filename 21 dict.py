#dictionary

dict1 = {'name':'sem','roll':47}
print(dict1)
print("key name : ",dict1['name'])

#update
dict1['name'] = 'kamlesh'
print("change the name : ",dict1)

dict1['nick'] = 'kl'
print("update the nick : ",dict1)

#delete

dict1.pop('nick')
print("pop the nick : ",dict1)


del dict1["name"]
print(dict1)
dict1['nick'] = 'kl'
#lenght
print("lenght of dict is : ",len(dict1))

#String

s = str(dict1)

print("str function in python : ",s)


#type

print("type func : ",type(dict1))
