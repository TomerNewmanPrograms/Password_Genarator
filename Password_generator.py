import string 
import random

#asks for the user a yes/no answer if the string parameter is allowed as an ingredient in the password
def isAllowed(characters):
    print("\nDo you want to include",characters,"write yes/no:  ")
    isInput = input()
    while isInput != "yes" and isInput != "Yes" and isInput != "YES" and isInput != "no" and isInput != "No" and isInput != "NO":
        print("\nfor",characters,"write only in yes/no:  ")
        isInput = input()

    if isInput == "yes" or isInput == "Yes" or isInput == "YES":
        return True
    else:
         return False

#returns a random char
def RandChar(FullListOfChars):
    return random.choice(FullListOfChars)
# calculates the strength level of the password in a scale between 1-4
def StrongPassLevel(Password):
    strength = 0
    for c in Password:
        if c.islower():
            strength+=1
            break
    for c in Password:
        if c.isupper():
            strength+=1
            break        
    for c in Password:
        if c in string.punctuation:
            strength+=1
            break  
    for c in Password:
        if c.isdigit():
            strength+=1
            break            
    return strength


print("\nWelcome, We will generate for you a Strong password.")
NumOfCharsInput = input("please enter the number characters in the password (at least 4):  ")
NumOfCharsInt = int(NumOfCharsInput)
isAllowedSymbols = isAllowed("Symbols")
isAllaowedNumbers = isAllowed("Numbers")
isAllaowedSmallLetters = isAllowed("Small Letters")
isAllaowedCapitalLetters = isAllowed("Capital Letters")

Password = ''
FullListOfChars = ''
PasswordStrength = 0

if (isAllowedSymbols==True):
    FullListOfChars += string.punctuation
    PasswordStrength += 1
if (isAllaowedNumbers==True):
    FullListOfChars += string.digits
    PasswordStrength += 1
if (isAllaowedSmallLetters==True):
    FullListOfChars += string.ascii_lowercase
    PasswordStrength += 1
if (isAllaowedCapitalLetters):
    FullListOfChars += string.ascii_uppercase
    PasswordStrength += 1

while  StrongPassLevel(Password) != PasswordStrength:
    Password = ''
    for i in range(0,NumOfCharsInt):
         Password = Password + RandChar(FullListOfChars)
    

print("\nTHE PASSWORD IS: ",Password)
