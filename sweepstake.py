

winner = ''


class Sweepstake:

    def __init__(self):
        self.name = ''
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants[len(self.contestants)] = contestant

    def pick_winner(self):
        import random
        winner = self.contestants[random.randint(0, len(self.contestants) - 1)]
        self.print_contestant_info(winner)
        return winner

    def print_contestant_info(self, contestant):
        print(f'{contestant.first_name} {contestant.last_name} congrats you have won the grand prize!')

