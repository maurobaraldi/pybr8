#!/usr/bin/env python

@profile
def potencia(expoente):
    for i in range(expoente):
        print '2^%i = %i' % (i, pow(2,i))


if __name__ == '__main__':
    potencia(10)
