from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager
sweepstakes_queue = SweepstakesQueueManager()
sweepstakes_stack = SweepstakesStackManager()

class MarketingFirmCreator:
    def __init__(self):
        self.name = ''

    def choose_manager_type(self):
        user_choice = input('do you want to choose your sweepstakes via a stack or queue?')
        if user_choice == 'stack':
            return sweepstakes_stack
        elif user_choice == 'queue':
            return sweepstakes_queue
        else:
            print('that was not a valid option.  please choose stack or queue')
            self.choose_manager_type()
