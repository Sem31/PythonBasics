# regular expression


import re

#check 'o' in 'Hello' are in or not
print("search 'o' in Hello")
match = re.search(r'.o','Hello')
if (match):
    print("found : ",match.group())
else:
    print("not found")

#print the strating three words
print("\w\w\w use this search three words in 'Hello'")
match = re.search(r'\w\w\w','Hello')
if (match):
    print("found : ",match.group())
else:
    print("not found")

#check the end of string is xyz yes or not
print("use $ to check end of string is xyz in 'Hello'")
match = re.search(r'$xyz','Hello')
if (match):
    print("found : ",match.group())
else:
    print("not found")

#
print("use ^ this check the Starting one with string 'Hello'")
match = re.search(r'^H','Hello')
if (match):
    print("found",match.group())
else:
    print("not found")
