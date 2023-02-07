import threading
import time
import  queue


some_list = [1, 10, 4, 3]
test_queue= queue.Queue

for item in some_list:
    test_queue.put(item)




class TestThread(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    # @staticmethod
    # def thread_count_down(name, delay):
    #     counter = 5
    #
    #     while counter:
    #         time.sleep(delay)
    #         print(f"Thread {name} counting: {counter}")
    #         counter -= 1
    @staticmethod
    def factors(item, name):
        result_string = f'{name} - Positive factors of {item} are: '
        for i in range(1, item + 1):
            if item % i == 0:
                result_string += str(i) + ' '
        result_string += '\n' + '_' * 20

        print(result_string)

    @staticmethod
    def process_queue(name):
        while True:
            if not test_queue.empty():

                item = test_queue.get(block=False)
                TestThread.factors(item, name)
            else:
                 return

    def run(self):
        print(f"Thread {self.name} STARTED")
        TestThread.process_queue(self.name)
        print(f"Thread {self.name} FINISHED")


thread1 = TestThread('A', 0.5)
thread2 = TestThread('B', 0.5)
thread3 = TestThread('c', 0.5)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()


