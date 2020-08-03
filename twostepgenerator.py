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
                shuffle = int(secrets.choice(numlist))
                for k in range(shuffle, -1, -1):
                        throwaway = ""
                        if k == 0:
                                cypherstring += secrets.choice(charlist)
                        else:
                                throwaway += secrets.choice(charlist)
                                del throwaway
        print(cypherstring)
        cypherstring = ""
