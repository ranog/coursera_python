#!/usr/bin/env python3

def ePrimo(k):

    i = 1
    num = 0
    count = 0
    
    while(i <= k):
        if(k % i == 0):
            count = count + 1

        i = i + 1

    if(count == 2):
        num = k
        
    return(num)

def maior_primo(n):
    if(n < 2):
        return False

    primo = ePrimo(n)

    if(primo == 0):

        while(primo == 0):
            n = n - 1
            primo = ePrimo(n)

        return(primo)
    
    else:
        return(primo)

