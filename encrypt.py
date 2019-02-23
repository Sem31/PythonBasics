import base64

str = "kamlesh"
str =  base64.b64encode(str.encode('utf-8'))
print("encoodeed =  ",str)
