from stack import Stack

stack = Stack()

class SweepstakesStackManager:
    def __init__(self):
        self.sweepstake_name = ''
        self.sweepstake_type = ''

    def insert_sweepstakes(self, sweepstake):
        stack.list.append(sweepstake)
        print(stack.list)


    def get_sweepstakes(self):
        # choose the sweepstake on the top of the stack return it
        pass
