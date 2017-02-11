from threading import Thread, Event
import time
import random

event_obj = Event()


def func_print(num, event):
    print 'start'
    time.sleep(random.randint(0, 3))
    event.wait()
    print 'thread {0} processed'.format(num)

if __name__ == '__main__':
    event_obj.clear()
    thread_list = [Thread(target=func_print, args=(i, event_obj), name='t.{0}'.format(i)) for i in range(20)]
    [t.start() for t in thread_list]

    # while filter(lambda x: not x.is_alive(), thread_list):
    #    thread_list time.sleep(1)

    print 'process halt'
    while raw_input('restart process?(y/n): ') != 'y':
        pass
    event_obj.set()
