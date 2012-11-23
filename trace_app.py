#!/usr/bin/env python

def trace_me(value):

    if value > 0:
        return 'positivo'
    elif value < 0:
        return 'negativo'
    else:
        return 'zero'

if __name__ == '__main__':
    trace_me(0)
