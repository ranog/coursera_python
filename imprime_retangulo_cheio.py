#!/usr/bin/env python3

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

aux = largura
while altura:

    while largura:
        print('#', end = '')
        largura -= 1

    print('')
    altura -= 1
    largura = aux


