from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager
from marketing_firm_creator import MarketingFirmCreator

marketing_firm_creator = MarketingFirmCreator()

class MarketingFirm:
    def __init__(self):
        #i am injecting the managers choice and the Marketing firm sweepstakes is dependant on that.  this allows for a smooth transition between a stack or queue function
        self.manager_choice = marketing_firm_creator.choose_manager_type()

    def create_sweepstakes(self):
        if self.manager_choice == 'queue':
            SweepstakesQueueManager.get_sweepstakes_queue(self)
        elif self.manager_choice == 'stack':
            SweepstakesStackManager.get_sweepstakes_stack(self)
        else:
            print('that is not a valid option')
            self.create_sweepstakes()
