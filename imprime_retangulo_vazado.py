#!/usr/bin/env python3

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

aux = largura
count = altura

while altura:

    if altura == count or altura == 1:
        while largura:
            print('#', end='')
            largura -= 1

    elif largura == aux:
        print('#', end='')

        while largura > 1: # para não imprimir um espaço em branco no final da
                           # linha o corretor dá erro se tiver.

            if largura == 2:
                print('#', end='')

            else:
                print(' ', end='')

            largura -= 1

    print('')
    altura -= 1
    largura = aux
