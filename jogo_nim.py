#!/usr/bin/env python3

# n = o número de peças inicial
# m = o número máximo de peças que é possível retirar em uma rodada

# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em
# deixar sempre múltiplos de (m+1) peças ao jogador oponente.

def computador_escolhe_jogada(N, M):

    if(N < M):
        return N

    i = 1
    while(i < M):
        if(((N-i) % (i + 1)) == 0):
            return i

        i = i + 1

    else:
        return M


def usuario_escolhe_jogada(N, M):
    SAI = int(input('Quantas peças você vai tirar? '))

    while(SAI > M or SAI > N):
        print('Oops! Jogada inválida! Tente de novo.')
        SAI = int(input('Quantas peças você vai tirar? '))

    return SAI


def partida():

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    i = 0
    while(i < n):
        if(((n - i) % (m + 1)) == 0):
            print('')
            print('Você começa')
            print('')
            jogador = usuario_escolhe_jogada(n, m)
            print('Você tirou', jogador, 'peças')
        else:
            print('')
            print('Computador começa')
            print('')
            computador = computador_escolhe_jogada(n, m)
            print('Computador tirou', computador, 'peças')

        i = i + 1


print('Bem-vindos ao Jogo do NIM! Escolha:')
print('')
jogo = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n'))
print('')

if(jogo == 1):
    partida()
