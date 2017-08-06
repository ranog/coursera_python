#!/usr/bin/env python3

import math

x1 = int(input("Digite X1: "))
y1 = int(input("Digite Y1: "))
x2 = int(input("Digite X2: "))
y2 = int(input("Digite Y2: "))

H = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if(H > 10):
    print("longe")

else:
    print("perto")
