#!/usr/bin/env python3

num = int(input("Digite um número inteiro: "))

i = 1
count = 0

while i <= num:
    if num % i == 0:
        count += 1

    i += 1

if count == 2:
    print("primo")
else:
    print("não primo")
