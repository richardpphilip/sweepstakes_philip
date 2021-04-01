from stack import Stack

stack = Stack()


class SweepstakesStackManager:
    def __init__(self):
        self.sweepstake_name = ''

    def insert_sweepstakes_stack(self, sweepstake):
        stack.list_stack.append(sweepstake)
        print(stack.list_stack)

    def get_sweepstakes_stack(self):
        chosen_sweepstake = stack.pop()
        print(chosen_sweepstake)
        return chosen_sweepstake
