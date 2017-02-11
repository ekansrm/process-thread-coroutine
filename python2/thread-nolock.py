import threading
import time


def func_print(num):
    time.sleep(1)
    print 'My numbner is {0}'.format(num)


if __name__ == '__main__':
    for i in range(0, 20, 1):
        t = threading.Thread(target=func_print, args=(i, ), name='t.{0}'.format(i))
        t.start()

