# Password-Encryption-Program
Encrypts passwords. What more do you need to know? lol

Version 0.1: 

Can only encrypt a single string of lower case letters.
Will add Upper case, numbers and special character support in later versions.
As well as making the encryption algorithm more complex

Encryption Algorithm:

1. Have user input their password 
2. Reverse the characters of the password 
3. Turn the letters into numbers (a = 0, b = 1, etc)
4. Increment the numbers by 7
4b. If the result is 26 or above then subtract the result by 8
5. Convert the new numbers back into letters 
6. Print the result from step 5 (The encrypted password)
