from threading import Thread
from multiprocessing import Process
import time


def f1():
    while True:
        print("f1 start")
        print(time.time())
        time.sleep(3)
        print("f1 finish")
        # yield '1'


def f2():
    while True:
        print("f2 start")
        print(time.time())
        time.sleep(3)
        print("f2 finish")
        # yield '2'


y = Thread(target=f1)
y.start()
x = Thread(target=f2)
x.start()
