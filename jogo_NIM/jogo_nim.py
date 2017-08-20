#!/usr/bin/env python3

# n = o número de peças inicial
# m = o número máximo de peças que é possível retirar em uma rodada

# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em
# deixar sempre múltiplos de (m+1) peças ao jogador oponente.


def computador_escolhe_jogada(n, m):

    if n <= m:
        return n

    result = n % (m+1)

    if not result:  # result == 0 == False
        return m

    return result



def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas peças você vai tirar? '))

    if jogada <= m and jogada >= 0:
        return jogada

    while jogada > m or jogada > n or jogada <= 0:
        print('Oops! Jogada inválida! Tente de novo.')

        jogada = int(input('Quantas peças você vai tirar? '))

    return jogada


def partida():

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    pecas_fora = 0  # peças fora do jogo

    vez_do_jogador = False

    if n % (m+1) == 0:
        vez_do_jogador = True

    if vez_do_jogador:
        print('\nVocê começa\n')
    else:
        print('\nComputador começa\n')

    msg = "{} retirou {} peças"

    while pecas_fora < n:
        if vez_do_jogador:
            pecas_retiradas = usuario_escolhe_jogada(n, m)

            print(msg.format('Você', pecas_retiradas))

            vez_do_jogador = False

        else:
            pecas_retiradas = computador_escolhe_jogada(n, m)

            print(msg.format('Computador', pecas_retiradas))

            vez_do_jogador = True

        pecas_fora += pecas_retiradas
        pecas_restantes = n - pecas_fora

        if pecas_restantes > 0:
            print('\nRestam {} peças\n'.format(pecas_restantes))


    if not vez_do_jogador:
        print('\nVoce venceu\n')
    else:
        print('\nComputador venceu\n')


def campeonato():

    print('\nVoce escolheu um campeonato!\n')

    i = 1
    while(i <= 3):
        print('\n**** Rodada ', i,' ****\n')

        partida()

        i += 1

    print('\n**** Final do campeonato! ****\n')
    print('\nPlacar: Você 0 X 3 Computador\n')


def run():
    print('Bem-vindos ao Jogo do NIM! Escolha:\n')
    jogo = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n\n'))

    if jogo == 1:
        partida()

    elif jogo == 2:
        campeonato()

    else:
        print("\n1 ou 2!!! Burro pra caralho!!!\n")


if __name__ == "__main__":
    run()
