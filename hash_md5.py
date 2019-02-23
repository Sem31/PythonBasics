import hashlib

str = "kamlesh"
hashkey = hashlib.md5(str.encode()).hexdigest()
print(hashkey)
