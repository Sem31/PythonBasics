import threading
import time

exitflag = 0
class mythread(threading.Thread):
    def __init__(self,Id,name,counter):
        threading.Thread.__init__(self)
        self.Id = Id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting : "+self.name)
        print_thread(self.name,self.counter,5)
        print("Ending : "+self.name)


def print_thread(threadname,delay,counter):
    while counter:
        if exitflag:
            threadname.exit()

        print("%s : %s"%(threadname, time.ctime(time.time())))
        time.sleep(delay)
        counter -= 1


thread1 = mythread(1,"thread-1",2)
thread2 = mythread(1,"thread-2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("exiting")


