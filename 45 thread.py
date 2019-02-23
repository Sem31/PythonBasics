import _thread
import time

def print_time(threadname,delay):
    count=0
    while count<5:
        count+=1
        print("%s : %s"%(threadname,time.ctime(time.time())))
        time.sleep(delay)


try:
    _thread.start_new_thread(print_time,("thread_1",2,))
    _thread.start_new_thread(print_time,("thread_2",2,))
except:
    print("Error: unable to start thread")
