from threading import *
import time
def demo_thread():
    time.sleep(3)
    print("hello")
t1 = Thread(target = demo_thread)
t1.start()
