# This program is called Enigma Machine 2.0. There is password feature that only allows only the Germans to encrypt and decrypt messages.
# For the name, please enter your name - FOR THE PASSWORD, PLEASE ENTER THE MINUTE YOU STARTED THE PROGRAM
# The current minute is the key shift. So every minute there will be a new shift - inspired by the The Imitation Game Movie 
# Enjoy the encryption program my fellow German comrades 

import datetime # import datetime module to reveal the current minute - refer to https://docs.python.org/2/library/datetime.html for the datetime module 
import time # import time for the delay statements  
import os # import os to open up the notepad file with the incrypted message 

now = datetime.datetime.now() # datetime.now use to find the current minute - to be used later in program 
print ("Welcome to the Enigma Machine 2.0")
FileName = input("Before we start, please enter a file name to save encrypted messages [no special characters]: ") + ".txt" # receive file name from user

def encrypt (FileName, input_message, key): # encryption function
    """encrypt(str, str, int) -> str
    Takes the message inputed by user, applies several changes, applies a shift based on the key (the minute) and prints the encryption out on a notepad file 
    >>> encrypt ('hello', 'aabbcc', 1)
    ddccbb! 
    """    
    my_file = open(FileName, "w") # opens the specific file name that the user previous wrote / write only file  
    
    letters = 'abcdefghijklmnopqrstuvwxyz' # string for all the alphabets 
    encryption = '' # initial encryption message 

    message = input_message[::-1] # takes the message written by user and reverses it. eg boy -> yob 
    message = message.replace(" ", "+") # takes the reversed message and replaced the spaces in between words with a plus sign "+"
    message = message + "!" # appends the str "!" to new message 
    

    for character in message: # scans through the each character of the message  
        if character in letters: # if the character is a letter 
            position = letters.find(character) # the position of the alphabet in message will be stored eg. a -> 0 
            newPosition = (position + key) % 26 # determines the new position of the letter with the key change (key = the minute) 
            newCharacter = letters[newPosition] # The new character based on the key shift 
            encryption += newCharacter # appends all of the letters to the encryption string 
        else:
            encryption += character # appends the rest of the characters into the string eg. ! and + 
    
    my_file.write(encryption) # prints out the encryption string on notepad 
    my_file.close() # close the file 
    os.startfile(FileName) # opens up notepad so the encrypted message can be viewed
    time.sleep(3) # delay by 3 seconds
    print("")
    main() # refers back to the main function 

def decrypt (FileName, key): # decryption function 
    """decrypt(str, int) -> str
    Takes the encrypted message, reverses several changes, substracts the shift based on the key and prints out the original message 
    >>> decrypt ('ddccbb!', 1)
    aabbcc
    """   
    letters = 'abcdefghijklmnopqrstuvwxyz' # string for all the alphabets  
    decryption = '' # initial decryption message 

    my_file = open(FileName, "r") # opens the specific file name / read only file  

    message = my_file.readline() # reads the encrypted message on the notepad file 
    
    message = message.replace("!", "") # takes the encrypted message and replaces the "!" with nothing 
    message = message[::-1] # takes the message and reverses it
    message = message.replace("+", " ") # takes the reversed message and replaces "+" with a space 
    
    for character in message: # scans through the each of the message 
        if character in letters: # if the character is a letter 
            new_position = letters.find(character)# the position of the alphabet in string letters will be stored eg a -> 1 
            old_Position = (new_position - key) % 26 # determines the old position of the letter with the key change (key = the minute) 
            oldCharacter = letters[old_Position] # The old character based on the key shift 
            decryption += oldCharacter # appends all of the letters to the decryption string 
        else:
            decryption += character # appends the rest of the characters into the string
    time.sleep(3) # delay by 3 seconds  
    decryption = "The decrypted code: " + decryption
    print(decryption)
    print("")
    main() # refers back to the main function 

def leave(): # the quit function
    """leave()-> str 
    Prints out Good Bye
    """
    print("Good Bye") # just prints good bye

def main(): # main function to allow user to choose which option needs to be performed
    """main()-> 
    Records the user inputs and depending on the input the output appears 
    """
    print("1. Write a message")
    print("2. Decrypt a message")
    print("3. Quit Program") 
    option = input("Your Option: ") # user inputs the number that corresponds the option they want
        
    if option == "1":
        input_message = str(input('Please input a message: ')).lower() # the user enters a message 
        key = int('%d' % now.minute) # the key will be stored as a numerical value based on the current minute 
        encrypt(FileName, input_message, key) # calls upon the encrypt function and passes the certain parameters. The varaibles are already stored.
    elif option == "2":
        if os.path.exists(FileName) == False: # checks if there is an encrypted message ready to decrypt 
            print ("There is nothing to decrypt. Please enter write a message first.") 
            main() # recall main()
        else:
            key = int('%d' % now.minute) # the key will be stored as a numerical value based on the current minute 
            decrypt(FileName, key) # calls upon the decrypt function and passes the certain parameters.  The varaibles are already stored.
    elif option == "3":
        print("Thank you for using Enigma Machine 2.0.") 
        leave() # closes the program 
    else:
        print("Invalid Input. Try Again.") # result if anything else is inputed by the user 
        main() # recall function again

def password_check():
    """password_check()-> str 
    Since only Germans can use the program. Intense sercurity is present. The user will enter the name and password (the minute the program was started).
    If the password is incorrect, the program will instantly shut down. If the password is correct continue to main(). 
    """
    x = True
    while x:
        Name = input ("Enter Name: ") # user enters a name 
        PassWord = input ("Enter Password: ") # user enters the password - the password is the minute the program was started. eg. if time is 11:17, enter 17 

        if PassWord == '%d' % now.minute: # checks if the password inputed is equal to the current minute 
            time.sleep(3) # delay by 3 seconds 
            print ("Login successful!")
            print ('')
            print ("Welcome", Name, "to Enigma Machine 2.0")
            x = False # makes x = false so the program only runs once
            main()
        else:
            print ("Password did not match!") # due to the harsh measure of Enigma Machine 2.0, the user is not allowed to retry the username and password 
            print ("PROGRAM TERMINATED")
            leave() # calls the leave function 
            break # stops while loop 
password_check() # call upon password_check function 
