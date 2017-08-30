#!/usr/bin/env python3

def e_primo(x):
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



limite = int(input('Limite máximo: '))
n = 2

while n < limite:
    if e_primo(n):
        print(n, end=' ')

    n += 1

print()
