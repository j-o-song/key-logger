import random 

class User: 
    ''' A class that represents a user

    Instance Attributes: 
    * id: user's unique indentification numeric string: str
    * full_name: user's first name and user's last name in lowercase; str
    * occurrence: the number of times user typed in secret code; int

    Class Attribute: 
    * user_list: a list of currently existing users and their id; dict<str, User>
    * id_length: length of the user ids: 
    '''
    user_dict = {}
    id_length = 3
    def __init__(self, full_name):
        self.id = str(random.randint(0, int('9' * User.id_length)))
        self.full_name = full_name
        self.occurrence = 0 

        if len(self.id) < User.id_length: 
            self.id = '0' * (User.id_length - len(self.id)) + self.id

        if len(User.user_dict) > 0:
            while self.id in User.user_dict.keys():
                self.id = str(random.randint(0, int('9' * User.id_length)))

        User.user_dict[self.id] = self
        
    def __str__(self): 
        return self.full_name + ' typed the code ' + str(self.occurrence) + ' times.'

    def __eq__(self, other):
        if self.id == other.id: 
            return True 
        return False