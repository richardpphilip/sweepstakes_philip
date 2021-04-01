from sweep_queue import Queue


queue = Queue()


class SweepstakesQueueManager:
    def __init__(self):
        self.sweepstakes_name = ''

    def insert_sweepstakes_queue(self, sweepstake):
        queue.list_queue.append(sweepstake)
        print(queue.list_queue)

    def get_sweepstakes_queue(self):
        chosen_sweepstake = queue.dequeue()
        print(chosen_sweepstake)
        return chosen_sweepstake

