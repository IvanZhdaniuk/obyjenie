import multiprocessing
import time


def some_func_1():
    p = multiprocessing.current_process()
    print(f'start process{name} with id {p.pid}')
    time.sleep(4)
    print(f'Exit process {p.name}')

def some_func_2():
    p = multiprocessing.current_process()
    print(f'start process{name} with id {p.pid}')
    time.sleep(2)
    print(f'Exit process {p.name}')


if __name__ = '__main__':
    p1 = multiprocessing.Process(name='Worcer 1' target=some_func_1)



