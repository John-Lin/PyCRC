#!/usr/bin/env python
import random
from pycrc.convert import *

class Sender(object):

    def __init__(self, dataword, divisor):
        self.divisor = divisor
        self.dataword = dataword
        self.remainder = 0
        self.codeword = 0
        self.arg_dataword = 0

    def getArgdataword(self):
        
        self.arg_dataword = self.dataword << count_bit(self.divisor)-1
        
        return dec2bin(self.arg_dataword)
        
    def generator(self):

        divisor_dec = bin2dec(self.divisor)

        arg_bit = count_bit(dec2bin(self.arg_dataword))
        div_bit = count_bit(self.divisor)

        xor_times = arg_bit - div_bit

        divisor_dec = divisor_dec << xor_times

        tmp = self.arg_dataword ^ divisor_dec
        
        divisor_dec = divisor_dec >> 1

        if tmp == 0:
            self.remainder = tmp
            return dec2bin(self.remainder)

        for i in range(1 ,xor_times):

            if (tmp ^ divisor_dec) > tmp:
                divisor_dec = divisor_dec >> 1
            else:
                tmp = tmp ^ divisor_dec
                divisor_dec >> 1

        self.remainder = tmp

        return dec2bin(self.remainder)

    def getCodeword(self):

        self.codeword = self.arg_dataword | self.remainder
        
        return dec2bin(self.codeword)


class Receiver(object):
    def __init__(self, codeword, divisor):
        
        self.codeword = codeword
        self.divisor = divisor
        self.syndrome = 0
        self.rx_dataword = 0

    def getDataword(self):
        
        self.rx_dataword = self.codeword >> count_bit(self.divisor)-1
        return dec2bin(self.rx_dataword)
    
    def checker(self):
        
        divisor_dec = bin2dec(self.divisor)

        code_bit = count_bit(dec2bin(self.codeword))
        div_bit = count_bit(self.divisor)

        xor_times = code_bit - div_bit

        divisor_dec = divisor_dec << xor_times

        tmp = self.codeword ^ divisor_dec
        
        divisor_dec = divisor_dec >> 1

        if tmp == 0:
            self.syndrome = tmp
            return dec2bin(self.syndrome)

        for i in range(1 ,xor_times):

            if (tmp ^ divisor_dec) > tmp:
                divisor_dec = divisor_dec >> 1
            else:
                tmp = tmp ^ divisor_dec
                divisor_dec >> 1

        self.syndrome = tmp

        return dec2bin(self.syndrome)

    def decision(self):
        self.rx_dataword = self.getDataword()

        
        if self.syndrome == 0:
            
            return False, self.rx_dataword
        else:

            return True, self.rx_dataword


class Channel(object):
    def __init__(self, codeword, rate=0.3):

        self.codeword = bin2dec(codeword)
        self.rate = rate
        self.rand = random.randint(1,101)
        self.noise = random.randint(1, self.codeword)
        self.rx_dataword = 0
        
    def passed(self):
        
        if self.rand > self.rate*100:
            self.rx_dataword = self.codeword
        
        elif self.rand > self.rate*100*0.5 and self.rand <= self.rate*100:
            self.rx_dataword = self.codeword | self.noise
        
        else:
            self.rx_dataword = self.codeword ^ self.noise

        return dec2bin(self.rx_dataword)

