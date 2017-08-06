#!/usr/bin/env python3

def fatorial(n):
    
    fator = 1

    while(n > 1):
        fator = fator * n
        n = n - 1

    return(fator)

def numero_binominal(n, k):
    return(fatorial(n) / (fatorial(k) * fatorial(n - k)))

def testa_fatorail():
    if(fatorial(1) == 1):
        print("Funciona para 1")
    else:
        print("Não Funciona para 1")

    if(fatorial(2) == 2):
        print("Funciona para 2")
    else:
        print("Não Funciona para 2")

    if(fatorial(0) == 1):
        print("Funciona para 0")
    else:
        print("Não Funicona para 0")

    if(fatorial(5) == 120):
        print("Funciona para 5")
    else:
        print("Não Funciona para 5")
