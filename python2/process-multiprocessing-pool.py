from multiprocessing import Pool
import time


def func_0(name):
    time.sleep(1)
    print 'My name is {0}'.format(name)


def func_1(name):
    print 'My name is {0}'.format(name)


if __name__ == '__main__':
    pool = Pool(processes=4)
    for i in range(0, 20, 1):
        pool.apply(func=func_0, args=('t_0.{0}'.format(i), ))

    for i in range(0, 20, 1):
        pool.apply_async(func=func_1, args=('t_1.{0}'.format(i), ))

    pool.close()
    pool.join()
