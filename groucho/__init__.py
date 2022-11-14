# GROUCHO by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import math
from math import floor

def reverse_array(array):
    """
    Reverses the order of an array 
    and returns the reversed array.
    """
    array.reverse()
    return array

def letter_index(letter):
    """
    Gets the index of a letter in the alphabet.
    Returns zero if the letter isn't in the 
    alphabet.
    """
    result = 0
    alphabetString = 'abcdefghijklmnopqrstuvwxyz'
    letterList = list(alphabetString)
    for i in letterList:
        if letter == i:
            result = letterList.index(i) + 1
        else:
            """
            Do nothing.
            """
    return result

def get_letter_from_index(index):
    """
    Gets the letter from a supplied index.
    Returns an empty string if a letter cannot be found.
    """
    result = ''
    alphabetString = 'abcdefghijklmnopqrstuvwxyz'
    letterList = list(alphabetString)
    for i in letterList:
        actualIndex = index - 1
        if actualIndex == letterList.index(i):
            result = i
        else:
            """
            Do nothing.
            """
    return result

def bin_to_dec(binaryNumber):
    """
    Converts a base 2 number to a base 10 number.
    """
    origDigitsList = list(binaryNumber)
    digitsList = reverse_array(origDigitsList)
    lenDigitsList = len(digitsList)
    decimalSum = 1
    decimalSum = 0;
    for i in range(0,lenDigitsList):
        if digitsList[i] == '1':
            toAdd = 2 ** i
            print(toAdd)
            decimalSum = decimalSum + toAdd
        else:
            """
            DO NOTHING!
            """
    result = str(decimalSum)
    return result

def dec_to_bin(decimalNumber):
    """
    Converts a base 10 number to a base 2 number.
    """
    endChars = []
    dec = decimalNumber
    initItem = dec % 2
    startDigit = str(initItem)
    endChars.append(startDigit)
    while floor(dec / 2) != 0:
      dec = floor(dec / 2)
      itemOneToAdd = dec % 2
      itemTwoToAdd = str(itemOneToAdd)
      endChars.append(itemTwoToAdd)
    reversedChars = reverse_array(endChars)
    result = ''.join(reversedChars)
    return result

def hex_to_dec(hexNumber):
    """
    Converts a base 2 number to a base 10 number.
    """
    base = 16;
    result = 0;
    digitSetString = '0123456789ABCDEF'
    digitSet = list(digitSetString)
    hexCharsBase = list(hexNumber)
    numberLength = len(hexCharsBase)
    hexChars = reverse_array(hexCharsBase)
    for i in range(0,numberLength):
        mulFactor = digitSet.index(hexChars[i])
        toAdd = int(mulFactor) * (16 ** i)
        result = result + toAdd
    return result

def is_bin(expr):
    """
    Checks whether the supplied number is 
    a binary number and returns a boolean based on this.
    """
    charList = ['1','0']
    exprCharList = list(expr)
    result = True
    for i in exprCharList:
        if i == charList[0] or i == charList[1]:
            """
            Do nothing.
            """
        else:
            result = False
    return result

def is_int(expr):
    """
    A function to check whether a string
    is an integer.
    """
    result = False
    if expr.isnumeric():
        result = True
    else:
        """
        DO NOTHING!
        """
    return result