from contestant import Contestant
from stack import Stack
from queue import Queue


class UserInterface:

    def __init__(self):
        self.name = ''
        self.stack = Stack()
        self.queue = Queue()

    def instantiate_contestant(self):
        Contestant.firstname = input('what is your first name?')
        Contestant.lastname = input('what is your last name?')
        Contestant.email = input('what is your email?')
        Contestant.registration_number = input("enter your registration number")
        return Contestant(Contestant.firstname, Contestant.lastname, Contestant.email, Contestant.registration_number)

    def instantiate_sweepstakes_stack(self):
        self.stack.list = input('What is the name of the sweepstakes you want to add?')
        return self.stack.list

    def instantiate_sweepstakes_queue(self):
        self.queue.list_queue = input('What is the name of the sweepstakes you want to add?')
        return self.queue.list_queue
