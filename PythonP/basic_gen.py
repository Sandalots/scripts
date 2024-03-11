#!/usr/bin/env python3
"""
Generates a random 9 character string of letters and numbers
"""

__author__ = "Sandy MacDonald"
__version__ = "0.1.0"
__license__ = "MIT"

import random
from word_list import word_list

symbol_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "£", "#", "$", "%", "^", "&", "*", "(", ")", '-', "+", "="]

def main():
    result = ""
    for x in range(9):
        random_choice = random.choice(symbol_table)
        result += str(random_choice)

    print(result)


if __name__ == "__main__":
    """ Outputs a random 9 character string of letters and numbers"""
    main()