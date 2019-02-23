import time
from http import cookies

c = cookies.SimpleCookie()

c['myCookie'] = "last access cookie time"

c['myCookie'] = time.asctime(time.localtime())
print(c)
