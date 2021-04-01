
class MarketingFirmCreator:
    def __init__(self):
        self.name = ''

    def choose_manager_type(self):
        user_choice = input('do you want to choose your sweepstakes via a stack or queue?')
        if user_choice == 'stack':
            return user_choice
        elif user_choice == 'queue':
            return user_choice
        else:
            print('that was not a valid option.  please choose stack or queue')
            self.choose_manager_type()
