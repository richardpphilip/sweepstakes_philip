from sweepstake import Sweepstake
from contestant import Contestant
from sweepstakes_stack_manager import SweepstakesStackManager
from stack import Stack
from user_interface import UserInterface


user_interface = UserInterface()
contestant1 = user_interface.instantiate_contestant()
contestant2 = user_interface.instantiate_contestant()
contestant3 = user_interface.instantiate_contestant()
sweepstake = Sweepstake()
sweepstake.register_contestant(contestant3)
sweepstake.register_contestant(contestant2)
sweepstake.register_contestant(contestant1)
sweepstake.pick_winner()
sweepstake1 = Stack('NJ power ball')
sweepstake2 = Stack('rich uncles giveaway')
#where should i create the sweepstake objects? in the stack
sweepstake_object = SweepstakesStackManager()
#cant get my sweepstakes to append to the the stack
Stack.push(sweepstake1)
Stack.push(sweepstake2)