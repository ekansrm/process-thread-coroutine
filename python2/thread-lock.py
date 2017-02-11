from threading import Thread, RLock
import time

g_sum = 0

r_lock = RLock()


def func_print(num):
    time.sleep(1)
    r_lock.acquire()
    global g_sum
    g_sum += num
    print 'My number is {0}'.format(num)
    print 'The sum is {0}'.format(g_sum)
    r_lock.release()


if __name__ == '__main__':
    [Thread(target=func_print, args=(i,), name='t.{0}'.format(i)).start() for i in range(0, 20, 1)]
