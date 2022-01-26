class Encrypter:

    def __init__(self, password):
        self.password = password
        self.pos = []
        self.shiftedAgain = 0
        self.shiftedPassword = []
        self.newVal = 0
        self.storeNewVal = []
        self.cypher = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
            "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
            "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20,
            "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,

            0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g",
            7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n",
            14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u",
            21: "v", 22: "w", 23: "x", 24: "y", 25: "z",

            #"A": 0.5, "B": 1.5, "C": 2.5, "d": 3, "e": 4, "f": 5, "g": 6,
            #"h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
            #"o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20,
            #"v": 21, "w": 22, "x": 23, "y": 24, "z": 25,

        }
    def reversePassword(self):

        return self.password[::-1]

    def convert(self, reversedPassword):

        convertedPassword = []

        for x in range(len(reversedPassword)):

            convertedPassword.append(self.cypher[reversedPassword[x]])

        return convertedPassword

    def shiftValue(self, convertedPassword):

        for x in range(len(convertedPassword)):

            self.newVal = convertedPassword[x] + 7

            if self.newVal >= 26:
                self.newVal -= 8
                self.storeNewVal.append(self.newVal)
                self.pos.append(x)
                self.shiftedAgain += 1

            self.shiftedPassword.append(self.newVal)

        return self.shiftedPassword

    def translate(self):

        translatedPassword = []

        for x in range(len(self.shiftedPassword)):
            translatedPassword.append(self.cypher[self.shiftedPassword[x]])


        return translatedPassword

    def decrypt(self):

        decryptedPassword = []

        for x in range(len(self.shiftedPassword)):

            if self.shiftedAgain == 0:
                decryptedPassword.append(self.cypher[self.shiftedPassword[x] - 7])

            if self.shiftedAgain > 0:
                self.shiftedPassword.pop(self.pos[x])
                self.shiftedPassword.insert(self.pos[x], self.storeNewVal[x] + 8)
                decryptedPassword.append(self.cypher[self.shiftedPassword[x] - 7])
                self.shiftedAgain -= 1


        return decryptedPassword


    def getPassword(self):
        return self.password