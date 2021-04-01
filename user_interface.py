from contestant import Contestant


class UserInterface:

    def __init__(self):
        self.name = ''

    def instantiate_contestant(self,):
        Contestant.firstname = input('what is your first name?')
        Contestant.lastname = input('what is your last name?')
        Contestant.email = input('what is your email?')
        Contestant.registration_number = input("enter your registration number")
        return Contestant(Contestant.firstname, Contestant.lastname, Contestant.email, Contestant.registration_number)
