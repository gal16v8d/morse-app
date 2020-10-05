import re
import string
from utils.letters import Letters

def showMorse(input):
    letters = Letters()
    result = ''
    for n in input:
        result += letters.convertToMorse(n)
    print('{0} en morse es: {1}'.format(input, result))

if __name__ == '__main__':
    userInput = input("Ingresa texto:")
    if re.match('^[a-zA-Z0-9]+$', userInput):
        nameArray = userInput.lower().split()
        showMorse(userInput)
    else:
        print('Texto no valido')
