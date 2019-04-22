import itertools
import math
import os
import time

# helps separate text visually
from termcolor import colored

def main():
    
    string_type = ''
    password = input("Please enter your password: ")
    wait(1)
    customize = input(
        "Would you like to customize the program to make it take shorter/longer to find your password? (suggested) ").lower()
    wait(1)
    if (customize in ["yes", 'yep', 'yea', 'sure']):

        using_caps = False
        using_nums = False
        symbols = False
        using_lower = False
        set_lower = False
        set_caps = False
        set_num = False
        set_symbols = False

        if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
            using_caps = True
        if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
            using_lower = True
        if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
            using_nums = True
        if "`" in password:
            symbols = True
        if "~" in password:
            symbols = True
        if "!" in password:
            symbols = True
        if "@" in password:
            symbols = True
        if "#" in password:
            symbols = True
        if "$" in password:
            symbols = True
        if "%" in password:
            symbols = True
        if "^" in password:
            symbols = True
        if "&" in password:
            symbols = True
        if "*" in password:
            symbols = True
        if "(" in password:
            symbols = True
        if ")" in password:
            symbols = True
        if "_" in password:
            symbols = True
        if "-" in password:
            symbols = True
        if "+" in password:
            symbols = True
        if "=" in password:
            symbols = True
        if "{" in password:
            symbols = True
        if "[" in password:
            symbols = True
        if "}" in password:
            symbols = True
        if "}" in password:
            symbols = True
        if "\\" in password:
            symbols = True
        if "|" in password:
            symbols = True
        if ";" in password:
            symbols = True
        if ":" in password:
            symbols = True
        if "'" in password:
            symbols = True
        if "\"" in password:
            symbols = True
        if "<" in password:
            symbols = True
        if "." in password:
            symbols = True
        if ">" in password:
            symbols = True
        if "," in password:
            symbols = True
        if "/" in password:
            symbols = True
        if "?" in password:
            symbols = True
        print("Please type in the number of the characters you would like the program to test for:")
        wait(1)
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Numbers")
        print("4. Symbols")
        print("5. All of the above")

        wait(1)
        selection = int(input("Please enter an option: "))
        if selection == 1:
            string_type += "abcdefghijklmnopqrstuvwxyz"
            set_lower = True
        
        elif selection == 2:
            string_type += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            set_caps = True
        
        elif selection == 3:
            string_type += "1234567890"
            set_num = True
        
        elif selection == 4:
            string_type += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\" "
            set_symbols = True
        
        elif selection == 5:
            string_type += "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\\ "
            set_lower = True
            set_caps = True
            set_num = True
            set_symbols = True

        if using_lower == True and set_lower == False:
            print()
            print(colored("Your password contains lowercase characters, but the program isn't set to look for them.","red"))
            wait(1)
            print(colored("This means that the program will never find your password", "red"))
            wait(1)
            
            lower = input("Turn on lowercase characters? ").lower()
            if lower == "yes" or lower == "yea" or lower == "yeah" or lower == "sure":
                string_type += "abcdefghijklmnopqrstuvwxyz"
                print()
                print(colored("Using lowercase letters.", "green"))
                wait(1)
        
        if using_caps == True and set_caps == False:
            print()
            print(colored("Your password contains uppercase characters, but the program isn't set to look for them.","red"))
            wait(1)
            print(colored("This means that the program will never find your password", "red"))
            wait(1)
            
            caps = input("Turn on uppercase characters? ").lower()
            if caps == "yes" or caps == "yea" or caps == "yeah" or caps == "sure":
                string_type += "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
                print()
                print(colored("Using uppercase letters.", "green"))
                wait(1)
        
        if using_nums == True and set_num == False:
            print()
            print(colored("Your password contains numbers, but the program isn't set to look for them.", "red"))
            wait(1)
            print(colored("This means that the program will never find your password", "red"))
            wait(1)
            
            nums = input("Turn on numbers? ").lower()
            if nums == "yes" or nums == "yea" or nums == "yeah" or nums == "sure":
                string_type += "1234567890"
                print()
                print(colored("Using numbers.", "green"))
                wait(1)
        
        if symbols == True and set_symbols == False:
            print()
            print(colored("Your password contains symbols, but the program isn't set to look for them.", "red"))
            wait(1)
            print(colored("This means that the program will never find your password", "red"))
            wait(1)
            useSyms = input("Turn on symbols? ").lower()
            if useSyms == "yes" or useSyms == "yea" or useSyms == "yeah" or useSyms == "sure":
                string_type += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\" "
                print()
                print(colored("Using symbols.", "green"))
                wait(1)

    else:
        string_type += "abcdefghijklmnopqrstuvwxyz "
        string_type += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string_type += "1234567890"
        string_type += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\""

    print(colored("Attempting to crack password...", "blue"))
    wait(2)
    if password == "":
        print(colored("You didn't specify a password! The program didn't even need to look.", "red"))
    else:
        tries, time_amount = tryPassword(password, string_type)
        time_amount1 = math.ceil(time_amount)
        if time_amount1 == 1:
            sec = "second"
        else:
            sec = "seconds"
        print()
        os.system('say "I can see your pass-crack"')
        print(colored("Cracked the password %s in %s tries and %s %s!" % (password, tries, time_amount1, sec),"green"))
        wait(1)
        tries = tries / time_amount
        tries = math.ceil(tries)
        print(colored("That's approximately %s guessed passwords per second!" % (tries), "green"))

# Brute force function
def tryPassword(passwordSet, string_typeSet):
    start = time.time()
    chars = string_typeSet
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if attempts % 5000000 == 0:
                if attempts > 999999999:
                    print()
                    stringAmount = str(attempts)
                    newList = list(stringAmount)
                    billions = int(newList[0])
                    billions2 = str(billions)
                    billions2 += "000000000"
                    billions2 = int(billions2)
                    millions = attempts - billions2
                    millions = millions / 1000000
                    millions = math.ceil(millions)
                    if attempts >= 50000000:
                        print("This could be a while....feel free to let this run")
                        print()
                    print("%s billion, %s million passwords guessed so far..." % (billions, millions))
                else:
                    print()
                    millions = attempts / 1000000
                    millions = math.ceil(millions)
                    if attempts > 50000000:
                        print("This could be a while....feel free to let this run")
                        print()
                    print("%s million passwords guessed so far..." % (millions))
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)

def wait(amount):
    time.sleep(amount)
    print()


main()



