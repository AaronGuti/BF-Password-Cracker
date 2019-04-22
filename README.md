# BF-Password-Cracker & Dictionary Attack 
A Brute-Force attack is method of breaking a cipher (that is, to decrypt a specific encrypted text) by trying every possible key. Feasibility of brute force attack depends on the key length of the cipher, and on the amount of computational power available to the attacker.

A dictionary attack is based on trying all the strings in a pre-arranged listing, typically derived from a list of words such as in a dictionary (hence the phrase dictionary attack). In contrast to a brute force attack, where a large proportion of the key space is searched systematically, a dictionary attack tries only those possibilities which are deemed most likely to succeed.


## Requirements 
* Python 3.6 
*The following packages installed:
  - colored (who doesn't like color coding)
  - hashlib
  - itertools
  - math
  - os (ony used for an alert on OSX)
  - time
  
### passCrack.py (long time)
This program exhaustively goes through every password possible until it matches the password that was entered by the user. The program keeps track of how many attempts are made as well as the time it takes to successfully guess the password.
### dictionary_atk.py (short time)
This program uses a newline separated file of common passwords to assist in guessing passwords. Typically when passwords are acquired they are hashed, so the user has the option to enter a hash as well as a plain text password that will be hashed after entering. The user input is then tested against all the password in the file that are hashed in the search. If the user input is contained in the file then a match will be found!
