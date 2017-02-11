from multiprocessing import Process, Manager


def add_num_to_array(name, num, arr):
    print 'My name is {0}'.format(name)
    arr = map(lambda x: x + num['arg1'], arr)
    print arr


def mul_num_to_array(name, num, arr):
    print 'My name is {0}'.format(name)
    arr = map(lambda x: x * num['arg1'], arr)
    print arr


if __name__ == '__main__':
    with Manager() as man:
        num = man.dict({'arg1': 3})
        arr = man.list(range(0, 20, 1))
        man = Manager()
        method_add = Process(target=add_num_to_array, args=('add', num, arr), name='add')
        method_mul = Process(target=mul_num_to_array, args=('mul', num, arr), name='mul')
        method_add.start()
        method_mul.start()
        method_add.join()
        method_mul.join()
