import string

class Letters:

    ALPHABET = list(string.ascii_lowercase)
    
    MORSE = ['·-','-···', '-·-·', '-··', '·',
    '··-·', '--·', '····', '··', '·---', '-·-',
    '·-··', '--', '-·', '---', '·--·', '--·-',
    '·-·', '···', '-', '··-', '···-', '·--',
    '-··-', '-·--', '--··']
    MORSE_INT = [
    '-----', '·----', '··---', '···--', '····-', 
    '·····', '-····', '--···', '---··', '----·' 
    ]

    def isInteger(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def posInAlphabet(self, input):
        try:
            return self.ALPHABET.index(input)
        except:
            return -1
    
    def convertToMorse(self, input):
        if (self.isInteger(input)):
            return self.MORSE_INT[int(input)]
        else:
            index = self.posInAlphabet(input)
            if (index != -1):
                return self.MORSE[index]
            else:
                return ''