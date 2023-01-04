from pynput import keyboard
import random 
import string
import User  

def generate_to_write(key):
    to_write = key
    if to_write == keyboard.Key.space: 
        to_write = ' '
    if to_write == keyboard.Key.enter:
        to_write = '\n'
    to_write = str(key).replace('\'', '')
    
    return to_write

def record_keystroke(key):
    ''' (Key) -> NoneType 
    Removes any single quotation from and writes string form of key (the current Key object) to
    keystroke_log.txt file. If key is the space key, writes white space to the file. If key is 
    the enter key, writes new line character to the file. 
    '''
    to_write = generate_to_write(key)
    with open('keystroke_log.txt', 'a') as key_file: 
        key_file.write(to_write)
    with open('keystroke_log.txt', 'r') as key_file: 
        content = key_file.read()
        if content[-code_length:] == code:
            user.occurrence += 1


def assess_keystrokes(key): 
    ''' (Key) -> NoneType 
    If key (the current Key object) is the escape key, stops the Listener. Also clears the file 
    with the recorded keystrokes and assesses if the user typed in a pre-defined code. If so,
    writes the users's name to a new file. 
    '''
    if key == keyboard.Key.esc: 
        listener.stop()
        if user.occurrence > 0: 
            with open('names.txt', 'a') as name_file: 
                name_file.write(first_name + ' ' + last_name + ':' + user.id + '\n')
        with open('keystroke_log.txt', 'a+') as key_file: 
            key_file.truncate(0)

def generate_random_code(code_length):
    ''' (int) -> str
    Returns a random string of English alphabets with length number of characters. 
    '''
    code = ''

    for i in range(code_length):
        code += string.ascii_lowercase[random.randint(0,26)]

    return code 

code_length = random.randint(2,10)
code = generate_random_code(code_length)
print(code)
first_name = input('What is your first name?: ').strip()
last_name = input('What is your last name?: ').strip()
full_name = first_name.lower() + ' ' + last_name.lower()
same_name = False
for dict_user in User.User.user_dict.values():
    if dict_user.full_name == full_name:
        same_name = True
        break 
if same_name:
    have_id = input('Do you have an ID? Type Yes/No: ') 
    if have_id.lower() == 'yes': 
        user_id = input('What is your ID?: ').strip()
        user = User.User.user_dict[user_id]
    elif have_id.lower() == 'no': 
        user = User.User(full_name)
        print('Your id is ' + user.id)
else: 
    user = User.User(full_name)
    print('Your id is ' + user.id)
print('Keylogging begins... To stop, click the esc key')
with keyboard.Listener(on_press=record_keystroke, on_release=assess_keystrokes) as listener: 
    listener.join()
print(user)
