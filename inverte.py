#!/usr/bin/env python3

"""
Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana, escreva um programa que
recebe uma sequência de números inteiros e imprima todos os valores em
ordem inversa. A sequência sempre termina pelo número 0. Note que 0
(ZERO) não deve fazer parte da sequência.
"""

sequencia = []

while True:
    numeros = int(input("Digite um número: "))
    if numeros == 0:
        break

    sequencia.append(numeros)


sequencia.reverse()

for numero in sequencia:
    print(numero)
