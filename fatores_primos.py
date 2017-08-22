#!/usr/bin/env python3

'''

Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores
primos, indicando também a mutiplicidade de cada fator.

8 = 2 * 2 * 2
20 = 2 * 2 * 5
1000 = 2 ^ 3 * 5 ^ 3

'''
n = int(input('Digite um número inteiro maior que 1: '))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n /= fator

    if multiplicidade > 0:
        print('fator ', fator, 'multiplicidade = ', multiplicidade)

    fator += 1
    multiplicidade = 0
