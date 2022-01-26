#Version 0.1 of Anti-Void's password encryption program. This is only the alpha version and I plan to add way more

#Current Features: only encrypts passwords that are all letters and lower case.

#Future Features: Users will be able to encrypt passwords with lower and upper case letters. As well
#As passwords with special characters and numbers. In addition, I'll add sentence encryption support
#as right now if you try to add spaces into the string, the program won't work.

from Encrypter import *

#Get password to encrypt from user
password = input("Type password to encrypt: ")

encryption = Encrypter(password)
#typedPassword = encryption.getPassword()

#Step 1: Reverse the inputted password
reversedPassword = encryption.reversePassword()

#Step 2: Convert the letters into numbers
convertedPassword = encryption.convert(reversedPassword)

#Step 3: Bump the value of each character by 7. If the value is 26 or above. Reduce the value by 8
shiftedPassword = encryption.shiftValue(convertedPassword)

#Step 4: Turn the values back into letters and then store in a variable.
#This Variable is the encrypted password
translatedPassword = encryption.translate()

#De-crypt the ecrypted password in order to make sure every step of the algorithm works
decryptedPassword = encryption.decrypt()

#Print("typed Password = " + typedPassword)
print("reversed password = " + reversedPassword)
print("converted password = " + str(convertedPassword))
print("shifted password = " + str(shiftedPassword))
print("encrypted password = ", end="")
for x in translatedPassword:
    print(x, end="")
print("")

print("decrypted password = ", end="")

x = int(len(decryptedPassword) - 1)
while x >= 0:
    print(decryptedPassword[x], end="")
    x -= 1
