import hashlib
import time
from termcolor import colored


counter = 1
h = hashlib.sha256()
h2 = hashlib.sha256()

choice = input(colored('Would you like to use a hash or a password? ', attrs=['bold']))

if choice.lower().strip() == 'hash' or choice.lower() == '4/20':
    pass_in = input("Please enter a hash: ")

elif choice.lower().strip() == 'password' or choice.lower() == 'pass' or choice.lower() == 'enter a password':
    pass_in = input("Please enter a password: ")
    pass_in.strip()
    h.update(pass_in.encode('utf-8'))
    pass_in = h.hexdigest()
    print(pass_in)

else:
    print(colored("\nThe choice you entered is not available.", 'red'))
    quit()

passFile = input('Please enter the password file name: ')
#
try:
    passFile = open(passFile, 'r')
except:
    print(colored("\nFile not found!", 'red'))
    quit()

for password in passFile:
    password = password.strip()
    setpass = password.encode('utf-8')
    hash_object = hashlib.sha256(setpass)
    filemd5 = hash_object.hexdigest()

    print(colored('Trying password #%d: %s' % (counter,password.strip()),'cyan'))


    counter += 1

    if pass_in.lower() == filemd5:
        print(colored('\nMatch found! \nPassword is: %s' % password, 'green'))
        break

else:
    print('Password not found.')