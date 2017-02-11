from multiprocessing import Process
import time


def func_print(num):
    time.sleep(1)
    print 'My numbner is {0}'.format(num)


if __name__ == '__main__':
    process_list = [Process(target=func_print, args=(i, ), name='t.{0}'.format(i)) for i in range(0, 20, 1)]
    process_start_rv_list = [t.start() for t in process_list]
    process_join_rv_list = [t.join() for t in process_list]
