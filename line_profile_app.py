#!/usr/bin/env python

@profile
def profile_me(limit):

    counter = 0

    while counter <= limit:
        counter = counter + 1

if __name__ == '__main__':
    profile_me(10)
