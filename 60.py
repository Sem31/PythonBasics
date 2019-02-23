# time and date 

import time

ticks = time.time()
print(ticks)

localtime = time.localtime(time.time())

print(localtime)

year = localtime[0]
month = localtime[1]
day = localtime[2]
print(day,"/",month,"/",year)

#excat time print
print(time.asctime(localtime))