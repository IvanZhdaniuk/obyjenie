import multiprocessing
import queue
import time


def count_down(name, delay):
    print(f"Process {name} started counting")
    counter = 5

    while counter:
        time.sleep(delay)
        print(f"Process {name} counts: {counter}")
        counter -= 1

    print(f"Process {name} finished counting")


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=count_down, args=("A", 0.5))
    process_2 = multiprocessing.Process(target=count_down, args=("B", 0.5))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
