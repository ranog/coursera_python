#!/usr/bin/env python3

n_int = int(input("Digite um número inteiro: "))

soma = 0

while(n_int):
    numero = n_int % 10
    soma = soma + numero
    n_int = n_int // 10

print(soma)
