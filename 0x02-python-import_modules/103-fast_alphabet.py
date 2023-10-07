#!/usr/bin/python3
def print_alphabet(char='A'):
        if ord(char) <= ord('Z'):
                    __import__('sys').stdout.write(char)
                            print_alphabet(chr(ord(char) + 1))

                            print_alphabet()

