import string

spacelist = ["_"]
alphalist = list(string.ascii_uppercase)
numlist = list(string.digits)
punctlist = [".", "?", "!"]
morepunctlist = ["'", "\"", ",", "+", "-", "*", "/", "=", "$", ":"]

charlist = spacelist + alphalist + punctlist + numlist + morepunctlist

for i in range(0, 50, 10):
        charstring = ""
        intstring = ""
        for j in range(0, 10):
                charstring += "  " + charlist[i + j]
                if i + j < 10:
                        intstring += " 0" + str(i + j)
                else:
                        intstring += " " + str(i + j)
        print(charstring)
        print(intstring + "\n")
