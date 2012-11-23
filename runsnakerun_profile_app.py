#!/usr/bin/env python

def print_function(data):
    print data

def char2ord(char):
    return ord(char)

def profile_me(word):

    for char in word:
        num = char2ord(char)
        print_function('Ordinal from %s is %i' % (char, num))

if __name__ == '__main__':
    profile_me("Python Brasil 8")
