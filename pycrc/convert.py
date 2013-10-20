#!/usr/bin/env python

def dec2bin(decimal):
    
    if type(decimal).__name__ == 'str':
        print "Error type : Not a integer"
        return 0

    digit = 1
    binary = 0

    decimal = int(decimal)

    while decimal != 0:
        binary = binary + (decimal%2) * digit
        decimal = decimal/2
        digit = digit * 10
    
    return str(binary)

def bin2dec(binary):

    if type(binary).__name__ == 'int':
        print "Error type : Not a string"
        return 0
    
    digit = 1
    decimal = 0

    binary = int(binary)

    while binary != 0:
        decimal = decimal + (binary%10) * digit
        binary = binary/10
        digit = digit * 2
    
    return decimal

def count_bit(value):
    
    if type(value).__name__ == 'int':
        binary = dec2bin(value)
        num_bits = len(binary)
    else:     
        num_bits = len(value)

    return num_bits
