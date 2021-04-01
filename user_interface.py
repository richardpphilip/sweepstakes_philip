from contestant import Contestant
from stack import Stack


class UserInterface:

    def __init__(self):
        self.name = ''
        self.stack = Stack()

    def instantiate_contestant(self,):
        Contestant.firstname = input('what is your first name?')
        Contestant.lastname = input('what is your last name?')
        Contestant.email = input('what is your email?')
        Contestant.registration_number = input("enter your registration number")
        return Contestant(Contestant.firstname, Contestant.lastname, Contestant.email, Contestant.registration_number)

    def instantiate_sweepstakes(self):
        self.stack.list = input('What is the name of the sweepstakes you want to add?')
        print(self.stack.list)
        return self.stack.list
