from time import sleep
import os
import signal

def f1():
    for i in range(3):
        sleep(2)
        print("写代码")


def f2():
    for i in range(2):
        sleep(4)
        print("测代码")


pld = os.fork()
if pld < 0:
    print("Process failed")
elif pld == 0:
    p = os.fork()
    if p == 0:
        f1()
    elif p > 0:
        os._exit(0)


else:

    os.wait()
    f2()