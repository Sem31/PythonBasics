import getpass
import hashlib

password = getpass.getpass("Entet the password : ")
h = hashlib.md5(password.encode())
print(h.hexdigest())
while password != "kamlesh@123":
    password = getpass.getpass("Entet the password : ")

if password == 'kamlesh@123':
    print("success")
else:
    print("Access Denied")
   