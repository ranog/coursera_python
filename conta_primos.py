#!/usr/bin/env python3

""" conta_primo.py

Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como
parametro e devolve a quantidade de números primos que existem entre 2 e n
(incluindo 2 e, se for o caso, n).
"""

__version__ = "$Revision: 0.01 $"
# $Source: /cvsroot/python/python/nondist/peps/pep-0008.txt,v $


def n_primos(num):



    primo = 1
    while primo <= num:

        item = 2
        while item <= num:
            if num % item == 0:
                count += 1



    return total
