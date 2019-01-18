import os
import time
from threading import Thread, Lock
import multiprocessing


def test(x, y):
    while True:
        # mutex.acquire()
        os.system('adb shell input tap {} {}'.format(x, y))
        # mutex.release()


def file_test():
    while True:
        # "dd if=/dev/input/event1 of=/sdcard/recordtap"
        cmd = 'adb shell "dd if=/sdcard/recordtap of=/dev/input/event1"'
        os.system(cmd)


if __name__ == '__main__':
    for i in range(10):
        # p = multiprocessing.Process(target=test, args=(544, 485))
        p = multiprocessing.Process(target=file_test)
        p.start()
    # for i in range(1000):
    #     cmd = 'adb shell "dd if=/sdcard/recordtap of=/dev/input/event1"'
    #     os.system(cmd)
    #     time.sleep(0.05)
