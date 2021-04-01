from sweepstake import Sweepstake
from contestant import Contestant
from sweepstakes_stack_manager import SweepstakesStackManager
from stack import Stack
from user_interface import UserInterface


user_interface = UserInterface()
# contestant1 = user_interface.instantiate_contestant()
# contestant2 = user_interface.instantiate_contestant()
# contestant3 = user_interface.instantiate_contestant()
# sweepstake = Sweepstake()
# sweepstake.register_contestant(contestant3)
# sweepstake.register_contestant(contestant2)
# sweepstake.register_contestant(contestant1)
# sweepstake.pick_winner()

sweepstake_object = SweepstakesStackManager()
sweepstake1 = user_interface.instantiate_sweepstakes()
sweepstake2 = user_interface.instantiate_sweepstakes()
sweepstake_object.insert_sweepstakes(sweepstake2)
sweepstake_object.insert_sweepstakes(sweepstake1)
sweepstake_object.get_sweepstakes()


