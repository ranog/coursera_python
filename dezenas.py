#!/usr/bin/env python3

n_str = input("Digite um número inteiro: ")
numero = int(n_str)

n_SemUnidade = numero // 10
n_Dezena = n_SemUnidade % 10

print("O dígito das dezenas é", n_Dezena)
