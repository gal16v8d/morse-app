import re
from utils.letters import Letters


def show_morse(input):
    letters = Letters()
    result = ''
    for n in input:
        result += letters.convert_to_morse(n)
    print('{0} en morse es: {1}'.format(input, result))


if __name__ == '__main__':
    user_input = input("Ingresa texto:")
    if re.match('^[a-zA-Z0-9]+$', user_input):
        name_array = user_input.lower().split()
        show_morse(user_input)
    else:
        print('Texto no valido')
