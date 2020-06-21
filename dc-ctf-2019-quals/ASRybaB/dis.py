#!/usr/bin/env python

# fish decoded the python byte code

from Crypto.Util import number

NSIZE = 1280

def create_key():
    if not False:

        # 29
        Nsize = NSIZE
        pqsize = Nsize / 2
        N = 0
        while N.bit_length() != Nsize:  # 51, loop
            while True:
                p = number.getStrongPrime(pqsize)
                q = number.getStrongPrime(pqsize)

                if (abs(p - q)).bit_length() > Nsize * 0.496:
                    break
            N = p * q
        phi = (p - 1) * (q - 1)

        limit1 = 0.261
        limit2 = 0.293
        while True:
            d = number.getRandomRange(pow(2, int(Nsize * limit1)), pow(2, int(Nsize * limit1) + 5))
            while d.bit_length() < Nsize * limit2:
                ppp = 0
                while not number.isPrime(ppp):
                    ppp = number.getRandomRange(pow(2, 45), pow(2, 45) + pow(2, 12))

                d *= ppp
            if number.GCD(d, phi) != 1:
                continue
            e = number.inverse(d, phi)
            if number.GCD(e, phi) != 1:
                continue
            break

        zzz = 3
    return (N, e)
