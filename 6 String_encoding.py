import base64

str = "kamlesh"

str = base64.b64encode(str.encode("utf-8"))
print("Encoded is : ",str)

str = base64.b64decode(str).decode("utf-8")
print("Decoded is : ",str)
