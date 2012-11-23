#!/usr/bin/env python

import cProfile

def profile_me(limit):

    counter = 0

    while counter <= limit:
        counter = counter + 1

if __name__ == '__main__':
    cProfile.run(profile_me(10))
