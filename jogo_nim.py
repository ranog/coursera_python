#!/usr/bin/env python3

# n == número de peças inicial.
# m == número máximo de peças que é possível retirar em uma rodada.


def computador_escolhe_jogada(n, m):

    return # interio correspondente à próxima jodada do computador de acordo com a estratégia vencedora


def usuario_escolhe_jogada(n, m):
    pecas = int(input("Quantas peças você vai tirar? "))

    while(pecas > m):
        Oops! Jogada inválida! Tente de novo.
        pecas = int(input("Quantas peças você vai tirar? "))
