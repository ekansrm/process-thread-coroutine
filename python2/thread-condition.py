from threading import Thread, Condition, RLock
import time


def consumer(conn):
    # must use 'with'
    with conn:
        print 'consumer before wait'
        conn.wait()
        print 'consumer after wait'


def producer(conn):
    # must use 'with'
    with conn:
        print 'producer before wait'
        conn.notifyAll()
        print 'producer after wait'


if __name__ == '__main__':

    condition = Condition()
    c1 = Thread(target=consumer, args=(condition, ), name='c1')
    c2 = Thread(target=consumer, args=(condition, ), name='c2')
    p = Thread(target=producer, args=(condition, ), name='p')

    c1.start()
    time.sleep(1)
    c2.start()
    time.sleep(1)
    p.start()

    condition2 = Condition(lock=RLock())

    c3 = Thread(target=consumer, args=(condition, ), name='c3')
    c4 = Thread(target=consumer, args=(condition, ), name='c4')
    p2 = Thread(target=producer, args=(condition, ), name='p2')

    c3.start()
    time.sleep(1)
    c4.start()
    time.sleep(1)
    p2.start()
