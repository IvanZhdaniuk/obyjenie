import multiprocessing

class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue =task_queue
        self.result_queue = result_queue

    def run(self):
        process_name= self.name

        while not self.task_queue.empty():

            task = self.task_queue.get()
            print(f'{process_name}')
            answer = task.process()
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task():
    def __init__(self, x):
        self.x = x

        def process(self):
            if self.x < 2:
                return f'is not prime number'
            if self.x


if __name__ == '__main__':
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    cpu_count = multiprocessing.cpu_count()
    consumers = [Consumer(tasks, results) for i in range(cpu_count)]

    for cons.start()
        tasks.put(Task(item))

    for i in range(len(some_list)):
        temp_result =


