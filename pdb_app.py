#!/usr/bin/env python

from pdb import set_trace

def debug_me(value):

    if value > 0:
        return 'positivo'
    elif value < 0:
        return 'negativo'
    else:
        return 'zero'

if __name__ == '__main__':
    set_trace() # Aqui ativa-se o debug 

    debug_me(0)
