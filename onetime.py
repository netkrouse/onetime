import string
from textwrap import wrap

spacelist = ["_"]
alphalist = list(string.ascii_uppercase)
numlist = list(string.digits)
punctlist = [".", "?", "!"]
morepunctlist = ["'", "\"", ",", "+", "-", "*", "/", "=", "$", ":"]

charlist = spacelist + alphalist + punctlist + numlist + morepunctlist

print("Encrypt or decrypt?\n\n1. Encrypt\n2. Decrypt")
userchoice = input()

if userchoice == "1":
        print("Enter cypher block, 50 characters per line:\n")
        cypherstring = ""
        for i in range(0, 20):
                cypher = input()
                cypherstring += cypher
        print("\nEnter plaintext:\n")
        plaintext = input()
        fixedplaintext = plaintext.ljust(1000, "_")
        encryptedstring = ""
        for j in range(0, 1000):
                encryptedvalue = charlist.index(fixedplaintext[j]) + charlist.index(cypherstring[j])
                encryptedmodulo = encryptedvalue % 50
                encryptedletter = charlist[encryptedmodulo]
                encryptedstring += encryptedletter
        encryptedblock = wrap(encryptedstring, 50)
        print("\n")
        for line in encryptedblock:
                print(line)

elif userchoice == "2":
        print("Enter cypher block, 50 characters per line:\n")
        cypherstring = ""
        for i in range(0, 20):
                cypher = input()
                cypherstring += cypher
        print("\nEnter encrypted text, 50 characters per line:\n")
        encryptedstring = ""
        for j in range(0, 20):
                encrypted = input()
                encryptedstring += encrypted
        decryptedstring = ""
        for k in range(0, 1000):
                decryptedvalue = charlist.index(encryptedstring[k]) - charlist.index(cypherstring[k])
                decryptedmodulo = decryptedvalue % 50
                decryptedletter = charlist[decryptedmodulo]
                decryptedstring += decryptedletter
        decryptedblock = wrap(decryptedstring, 50)
        print("\n")
        for line in decryptedblock:
                print(line)

else:
        print("Invalid choice")
