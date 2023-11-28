'''Allows to get morse value of any valid input'''
import re
import string
from typing import Any


ALPHABET = list(string.ascii_lowercase)
MORSE = ['·-', '-···', '-·-·', '-··', '·',
         '··-·', '--·', '····', '··', '·---', '-·-',
         '·-··', '--', '-·', '---', '·--·', '--·-',
         '·-·', '···', '-', '··-', '···-', '·--',
         '-··-', '-·--', '--··']
MORSE_INT = ['-----', '·----', '··---', '···--', '····-',
             '·····', '-····', '--···', '---··', '----·']


def is_integer(value: Any):
    '''Return true if value is int, false otherwise'''
    return isinstance(value, int)


def pos_in_alphabet(value: string):
    '''Return index of value inside ALPHABET arr, -1 otherwise'''
    return ALPHABET.index(value) if value in ALPHABET else -1


def convert_to_morse(value: Any):
    '''Return morse result of single value input'''
    if is_integer(value):
        return MORSE_INT[int(value)]
    index = pos_in_alphabet(value)
    return MORSE[index]if index != -1 else ''


def show_morse(value: Any):
    '''Return morse result of full value input'''
    result = ''
    for n in value:
        result += convert_to_morse(n)
    print(f'{value} en morse es: {result}')


if __name__ == '__main__':
    user_input = input('Ingresa texto:')
    if re.match('^[a-zA-Z0-9]+$', user_input):
        name_array = user_input.lower().split()
        show_morse(user_input)
    else:
        print('Texto no valido')
