from contestant import Contestant

contestant1 = Contestant('Rich', 'Philip', 'richardphilip@email.com', 1)
contestant2 = Contestant('Regina', 'Wang', 'reginawang@email.com', 2)



class Sweepstake:

    def __init__(self):
        self.name = ''
        self.contestants = {}

    # trying to add the dictionaries of the contestants into a multi - dimensional dictionary
    def register_contestant(self, contestant):
        self.contestants[len(self.contestants)] = contestant

    def pick_winner(self):
        import random
        winner = self.contestants[random.randint(0, 2)]
        print(winner.first_name)
        print(winner.last_name)
        return winner

    def print_contestant_info(self, contestant):
        # prints out the winning contestant
        pass



