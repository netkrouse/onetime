import string
import secrets

spacelist = ["_"]
alphalist = list(string.ascii_uppercase)
numlist = list(string.digits)
punctlist = [".", "?", "!"]
morepunctlist = ["'", "\"", ",", "+", "-", "*", "/", "=", "$", ":"]

charlist = spacelist + alphalist + punctlist + numlist + morepunctlist

cypherstring = ""

for i in range(0, 20):
        for j in range(0, 50):
                cypherstring += secrets.choice(charlist)
        print(cypherstring)
        cypherstring = ""
