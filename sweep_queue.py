class Queue:

    def __init__(self):
        self.list_queue = ['lottery', 'raffle', 'auction']

    def enqueue(self, item):
        self.list_queue.append(item)

    def dequeue(self):
        return self.list_queue.pop(0)
