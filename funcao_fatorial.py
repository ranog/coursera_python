#!/usr/bin/env python3

def fatorial(fator):

    fat = 1
    count = 1

    while count <= fator:

        fat *= count
        count += 1

    return fat


numero = 1

while numero >= 0:

    numero = int(input("Digite um numero: "))

    if numero < 0:
        break

    resultado = fatorial(numero)
    print(resultado)
