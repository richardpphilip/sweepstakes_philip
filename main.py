from sweepstake import Sweepstake
from contestant import Contestant
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager
from stack import Stack
from user_interface import UserInterface
from marketing_firm_creator import MarketingFirmCreator
from marketing_firm import MarketingFirm

user_interface = UserInterface()
#GIVES ABILITY FOR USER TO ADD CONTESTANT TO DRAWING
# contestant1 = user_interface.instantiate_contestant()
# contestant2 = user_interface.instantiate_contestant()
# contestant3 = user_interface.instantiate_contestant()
# sweepstake = Sweepstake()
# sweepstake.register_contestant(contestant3)
# sweepstake.register_contestant(contestant2)
# sweepstake.register_contestant(contestant1)
#PICKS WINNER FROM POOL
# sweepstake.pick_winner()
#GIVES ABILITY FOR USER TO ADD SWEEPSTAKES TO STACK
# sweepstake_object_stack = SweepstakesStackManager()
# # sweepstake1 = user_interface.instantiate_sweepstakes_stack()
# # sweepstake2 = user_interface.instantiate_sweepstakes_stack()
# # sweepstake3 = user_interface.instantiate_sweepstakes_stack()
# # sweepstake_object_stack.insert_sweepstakes_stack(sweepstake1)
# # sweepstake_object_stack.insert_sweepstakes_stack(sweepstake2)
# # sweepstake_object_stack.insert_sweepstakes_stack(sweepstake3)
# PRINTS LAST OBJECT ADDED TO STACK
# # sweepstake_object_stack.get_sweepstakes_stack()
#GIVES ABILITY FOR USER TO ADD SWEEPSTAKES TO QUEUE
# sweepstake_object_queue = SweepstakesQueueManager()
# sweepstake4 = user_interface.instantiate_sweepstakes_queue()
# sweepstake5 = user_interface.instantiate_sweepstakes_queue()
# sweepstake6 = user_interface.instantiate_sweepstakes_queue()
# sweepstake_object_queue.insert_sweepstakes_queue(sweepstake4)
# sweepstake_object_queue.insert_sweepstakes_queue(sweepstake5)
# sweepstake_object_queue.insert_sweepstakes_queue(sweepstake6)
# PRINTS FIRST OBJECT ADDED TO QUEUE
# sweepstake_object_queue.get_sweepstakes_queue()
# PRINTS FIRST OBJECT ADDED TO STACK

def run_simultation():
    marketing_firm = MarketingFirm()
    marketing_firm.create_sweepstakes()


# run_simultation()
