from stack import Stack


class SweepstakesStackManager:
    def __init__(self):
        self.sweepstake_name = ''
        self.sweepstake_type = ''

    def insert_sweepstakes(self, sweepstake):
        Stack.stack.append(sweepstake)

    def get_sweepstakes(self):
        # choose the sweepstake on the top of the stack return it
        pass
