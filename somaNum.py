#!/usr/bin/env python3

numero = int(input("Digite um número inteiro: "))

soma = 0

while(numero != 0):
    soma = soma + numero % 10
    numero = numero // 10
    
print("Soma dos números é", soma)
