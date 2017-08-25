#!/usr/bin/env python3

def ePrimo(x):
    fator = 2

    if x == 2:
        return True

    elif x == 1:
        return False

    while x % fator != 0 and fator <= x / 2:
        fator += 1

    if x % fator == 0:
        return False

    else:
        return True


n = True

while n:
    n = int(input('Digite um número inteiro: '))

    if ePrimo(n):
        print(n, 'é primo!')

    else:
        print(n, 'não é primo.')
