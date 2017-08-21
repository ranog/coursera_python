#!/usr/bin/env python3

numero = 1

while numero >= 0:

    numero = int(input("Digite um numero: "))
    count = 1
    fatorial = 1

    while count <= numero:
        fatorial *= count
        count += 1

    print(fatorial)
