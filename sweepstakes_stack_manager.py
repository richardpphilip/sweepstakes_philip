from stack import Stack

stack = Stack()


class SweepstakesStackManager:
    def __init__(self):
        self.sweepstake_name = ''

    def insert_sweepstakes(self, sweepstake):
        stack.list.append(sweepstake)
        print(stack.list)

    def get_sweepstakes(self):
        chosen_sweepstake = stack.pop()
        print(chosen_sweepstake)
        return chosen_sweepstake
