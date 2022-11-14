# GROUCHO by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from pyzeppo import *

def testAll():
    """
    Tests all of the functions that
    Groucho provides.
    """
    testArray = [1,2,3,4]
    print(reverse_array(testArray))
    testLetter = 'b'
    print(letter_index(testLetter))
    print(get_letter_from_index(letter_index(testLetter)))
    binaryNum = '101010'
    print(bin_to_dec(binaryNum))
    print(dec_to_bin(21))
    testHexNum = '000A00'
    testBinNum = '1010101'
    impostorBin = '1010101A'
    testInt = '10'
    impostorInt = 'AB'
    print(hex_to_dec(testHexNum))
    print(is_bin(testBinNum))
    print(is_bin(impostorBin))
    print(is_int(testInt))
    print(is_int(impostorInt))

def main():
    testAll()

main()
