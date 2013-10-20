#!/usr/bin/env python
from pycrc.convert import *
#from pycrc.crclib import Sender, Receiver, Channel
from pycrc.crclib import Sender, Receiver, Channel
def main():

    divisor = str(raw_input("Input divisor in binary type: "))
    #user_dataword = str(raw_input("Input dataword in binary type: "))
    user_dataword = '1001'

    print "\nSender:"
    
    dataword = Sender(bin2dec(user_dataword), divisor)
    arg_dataword = dataword.getArgdataword()
    remainder = dataword.generator()
    codeword = dataword.getCodeword()
    
    print "arg_dataword:", arg_dataword
    print "remainder:", remainder
    print "codeword:", codeword



    print "\nChannel:"

    channel = Channel(codeword)
    channel_codeword = channel.passed()
    print "Throgh to the channel get codeword:", channel_codeword
    



    print "\nReceiver:"

    rx_codeword = Receiver(bin2dec(channel_codeword), divisor)
    #rx_dataword = rx_codeword.getDataword()
    syndrome = rx_codeword.checker()
    ans, rx_dataword = rx_codeword.decision()
    
    print "syndrome:", syndrome
    print "Discard or not?", ans
    print "rx_dataword:", rx_dataword

if __name__ == '__main__':
    main()