#!/usr/bin/python2.7

"""
Input Description

A string of n a's
Output Description

Print the string at each step. The last line should be "a" (assuming the Collatz conjecture)
Challenge Input

aaa
aaaaa
Challenge Output

aaa

#############

2-tag system
    Alphabet: {a,b,c}
    Production rules:
         a  -->  bc
         b  -->  a
         c  -->  aaa


Computation
    Initial word: aaa <--> n=3
                    abc
                      cbc
                        caaa
                          aaaaa  <--> 5
                            aaabc
                              abcbc
                                cbcbc
                                  cbcaaa
                                    caaaaaa
                                      aaaaaaaa  <--> 8
                                        aaaaaabc
                                          aaaabcbc
                                            aabcbcbc
                                              bcbcbcbc
                                                bcbcbca
                                                  bcbcaa
                                                    bcaaa
                                                      aaaa  <--> 4
                                                        aabc
                                                          bcbc
                                                            bca
                                                              aa  <--> 2
                                                                bc
                                                                  a  <--> 1
                                                                   (halt)



###############

"""

input_string = raw_input("Enter a string of n a's ")

arules = bc
brules = a
crules = aaa

while input_string != 'a':
    if symbol == a:
        append = arules
    elif symbol == b:
        append = brules
    else:
        append = crules
    symbol = symbol[1:] + append
    Print symbol
