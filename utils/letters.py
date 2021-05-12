import string


class Letters:

    ALPHABET = list(string.ascii_lowercase)

    MORSE = ['·-', '-···', '-·-·', '-··', '·',
             '··-·', '--·', '····', '··', '·---', '-·-',
             '·-··', '--', '-·', '---', '·--·', '--·-',
             '·-·', '···', '-', '··-', '···-', '·--',
             '-··-', '-·--', '--··']
    MORSE_INT = [
        '-----', '·----', '··---', '···--', '····-',
        '·····', '-····', '--···', '---··', '----·'
    ]

    def is_integer(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def pos_in_alphabet(self, input):
        try:
            return self.ALPHABET.index(input)
        except:
            return -1

    def convert_to_morse(self, input):
        if (self.is_integer(input)):
            return self.MORSE_INT[int(input)]
        else:
            index = self.pos_in_alphabet(input)
            if (index != -1):
                return self.MORSE[index]
            else:
                return ''
