from sweepstake import Sweepstake
from contestant import Contestant
from user_interface import UserInterface
contestant1 = Contestant('Rich', 'Philip', 'richardphilip@email.com', 1)
contestant2 = Contestant('Regina', 'Wang', 'reginawang@email.com', 2)
contestant3 = Contestant('Laura', 'Philip', 'laura.philip@email.com', 3)

sweepstakes = Sweepstake()
sweepstakes.register_contestant(contestant1)
sweepstakes.register_contestant(contestant2)
sweepstakes.register_contestant(contestant3)
sweepstakes.pick_winner()
