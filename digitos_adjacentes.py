#!/usr/bin/env python3

num = int(input("Digite um número inteiro: "))

count = 0
i = 0
j = 0

while(num != 0):
    i = num % 10
    num = num // 10
    j = num % 10

    if(i == j):
        count = count + 1 

if(count == 0):
    print("não")

else:
    print("sim")
