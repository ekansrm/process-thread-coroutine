import threading
import time


def func_print(num):
    time.sleep(1)
    print 'My numbner is {0}'.format(num)


if __name__ == '__main__':
    for i in range(0, 20, 1):
        t = threading.Thread(target=func_print, args=(i, ), name='t.{0}'.format(i))
        t.start()

    #
    '''
My numbner is 4My numbner is 14My numbner is 5
My numbner is 2My numbner is 3My numbner is 0

My numbner is 1
My numbner is 10
My numbner is 15
 My numbner is 8
 My numbner is 13

My numbner is 7
 My numbner is 11

 My numbner is 6

My numbner is 12My numbner is 17
My numbner is 9

My numbner is 19
My numbner is 18
 My numbner is 16
    '''

