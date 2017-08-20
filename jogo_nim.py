#!/usr/bin/env python3

# n = o número de peças inicial
# m = o número máximo de peças que é possível retirar em uma rodada

# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em
# deixar sempre múltiplos de (m+1) peças ao jogador oponente.


def computador_escolhe_jogada(pecas, max_pecas):

    if pecas < max_pecas:
        return pecas

    result = pecas % (max_pecas + 1)

    if not result:
        return max_pecas

    return result


def usuario_escolhe_jogada(pecas, max_pecas):
    jogada = int(input('Quantas peças você vai tirar? '))

    while jogada > max_pecas or jogada > pecas or jogada < 0:
        print('Oops! Jogada inválida! Tente de novo.')

        jogada = int(input('Quantas peças você vai tirar? '))

    return jogada


def partida():

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    retiradas = 0 # peças retiradas no jogo
    jogador = False

    if n % (m + 1) == 0:
        jogador = True

    if jogador:
        print('\nVocê começa\n')
    else:
        print('\nComputador começa\n')

    msg = '{} retirou {} peças'

    while n:
        if jogador:
            retiradas = usuario_escolhe_jogada(n, m)

            print(msg.format('Você', retiradas))

            n -= retiradas

            jogador = False

        else:
            retiradas = computador_escolhe_jogada(n, m)

            print(msg.format('Computador', retiradas))

            n -= retiradas

            jogador = True

        if n > 0:
            print('\nRestam {} peças\n'.format(n))

    if not jogador:
        print('\nVocê venceu\n')
    else:
        print('\nComputador venceu\n')


def campeonato():
    print('\nVocê escolheu um campeonato!\n')

    count = 0

    while count <= 3:
        print('\n**** Rodada ', count,' ****\n')

        partida()

        count += 1

    print('\n**** Final do campeonato! ****\n')
    print('\n\Placar: Você 0 X 3 Computador\n')

def run():
    print('Bem-vindos ao Jogo do NIM! Escolha:\n')

    jogo = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n\n'))

    if jogo == 1:
        partida()

    elif jogo == 2:
        campeonato()

    else:
        print('\n1 ou 2!!! Burro para um caralho!!!\n')

if __name__ == "__main__":
    run()

