#!/usr/bin/env python3

# n = o número de peças inicial
# m = o número máximo de peças que é possível retirar em uma rodada

# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em
# deixar sempre múltiplos de (m+1) peças ao jogador oponente.

def computador_escolhe_jogada(N, M):
    SAI = M

    if(N < M):
        return N


    while(M > 0):
        if(N % (M + 1) == 0):
            return M

        M = M - 1

    else:
        return SAI

def usuario_escolhe_jogada(N, M):
    SAI = int(input("Quantas peças você vai tirar? "))

    while(SAI > M or SAI > N):
        print("Oops! Jogada inválida! Tente de novo.")
        SAI = int(input("Quantas peças você vai tirar? "))

    return SAI

def partida():
    n = int(input("Quantas peças? ")
    m = int(input("Limite de peças por jogada? ")

    if((n % (m + 1)) == 0):
        print("Você começa")
        i = 0
    else:
        print("Computador começa")
        i = 1


E o que tem a função partida? Partida é a função que vai perguntar os valores
de n e m que estão valendo para aquela partida. É também a partida que vai
decidir quem é que começa o jogo. Se é o computador ou o usuário de acordo com
aquela regra lá e é também quem vai ser responsável por chamar as funções
computador_escolhe_jogada, usuario_escolhe_jogada, computador_escolhe_jogada,
usuario_escolhe_jogada alternadamente até o jogo terminar. Ou seja, essa
função vai ter laço que vai fazer essas chamadas. E essa função é que vai
pegar o valor devolvido pelas funções usuario_escolhe_jogda e
computador_escolhe_jogada e atualizar o valor de n de acordo. Tinha tantas
peças no tabuleiro esse jogador ou computador tirou tantas peças, agora o n
vale tanto. E aqui identifica portanto que o jogo acabou. Opa, n chegou no
zero, não tem mais nenhuma peça no tabuleiro, o jogo acabou. E o que que tem?
Tem campeonato também. Só o que o campeonato precisa fazer é chamar a função
partida três vezes. Não precisa você criar dentro de campeonatos repetir a
lógica que tem partida. Não, partida já está pronto. Você só vai chamar
partida três vezes na função campeonato. Quais são alguns erros comuns que as
pessoas fazem quando tentam resolver o jogo do NIM. Primeiro, você fala assim:
    eu tenho que alternar entre os jogadores. Jeito que eu posso fazer é
    dentro de computador_escolhe_jogada eu faço a jogada e já chamo o
    usuario_escolhe_jogada. E dentro do usuario_escolhe_jogada eu faço a
    jogada e já chamo computador_escolhe_jogada. Isso até poderia funcionar,
    mas se você fizer assim as funções não vão devolver nada. E o que o
    enunciado espera é que você devolva o valor removido cada interação. Outra
    coisa que as pessoas erram muito comumente. A função alguém
    aí_escolhe_jogada devolve o número de peças que sobrou no tabuleiro. Não.
    É para devolver o número de peças que foi removido naquela jogada. O que
    mais? Tenta tratar os valores de n e m como variáveis globais, que todo
    mundo acessa essas variáveis. Não é para trabalhar assim, porque afinal de
    contas você está recebendo nas funções n e m como parâmetro, certo? Então
    é para você usar esses parâmetros, você não precisa pensar n e m como
    variáveis globais. Fora que se você pensar n e m como variáveis globais,
    aí aquelas duas funções computador_escolhe_jogada e usuario_escolhe_jogada
    deixariam de ser independentes, elas iam parar de funcionar fora do
    programa e isso não vai dar certo também. Algumas dicas e algumas
    coisinhas a levar consideração enquanto vocês estão fazendo o exercício.
    Primeiro: você as vezes cria todas as funções que foram pedidas no
    enunciado, mas se você não chamar alguma função o jogo não começa. Ou você
    começa fazendo 'print, bem vindo ao jogo do NIM. Escolha dois, tal' e aí
    você vai chamar partida de campeonato, ou então você pode criar uma função
    principal que chama jogo, main, início, o nome que você quiser, que aí vai
    ter essa parte aí dentro- bem vindo, escolha e tal- e aí você tem que
    chamar esta função. Você chama função jogo, ou main ou início. Outra coisa
    que é uma dica interessante: como é que faz para verificar se a entrada do
    usuário é valida? Bom, a gente já fez alguns laços que é assim: repita
    aquilo ali até o usuário digitar zero, por exemplo. Você pode fazer:
        repita até o usuário digitar valor válido. Então você vai checando se
        o valor é válido, enquanto o valor que o usuário digitou não for
        válido, você vai repetindo até ele digitar valor válido. E muita
        atenção, tem vários tipos de erro que o usuário pode fazer. Não é
        qualquer valor que o usuário pode colocar que é válido. Você tem que
        verificar todos os casos inválidos que pode acontecer. Preste atenção
        porque o corretor automático faz algumas tentativas de jogadas
        inválidas que não são muito óbvias, mas que servem para você ter a
        dica: isso aqui eu não lembrei e você pode corrigir função do que o
        corretor automático vai responder quando ele fizer a correção. E o que
        mais que tem? O corretor automático dá algumas mensagens. Vou dar uma
        passada algumas aqui para vocês entenderem o que ele está fazendo. Uma
        mensagem que ele faz é essa aqui: testando uma ligação de entrada do
        usuário. N igual a tanto, m igual a tanto, resposta: tanto. O que que
        ele está fazendo aqui? Ele está chamando usuario_escolhe_jogada com os
        parâmetros x e y e aí ele está tentando digitar, ele faz de conta que
        ele é usuário digitando o valor Z. Então se você tiver uma mensagem de
        corretor automático envolvendo esse tipo de mensagem, você sabe o que
        ele está testando e aí você pode entender: com esses valores de x e y
        ele tentou z e o meu programa não acertou por alguma razão. Outra
        mensagem que ele faz: testando jogada do computador, com n igual a x e
        m igual a y. Mesma coisa, ele está rodando computador_escolhe_jogada e
        passando os parâmetros x e y. Outra mensagem que ele dá: checando
        partida única. N igual a x, m igual y, jogadas, tal. O que ele está
        fazendo? Ele está rodando o programa, escolhendo a opção que é partida
        única, passando os valores x e y, que são m e n, que no começo do
        programa o jogo pede isso e aí ele faz as jogadas. Ele joga a, b, c,
        ele está jogando com o computador. Ele tenta simular uma partida. E
        tem a mensagem 'checando o campeonato' que ele faz a mesma coisa, só
        que ao invés de ele escolher a opção ele escolhe a opção dois e aí ele
        roda três partidas seguidas com n, m, os valores que ele vai indicar
        lá. Além disso você precisa lembrar que o exercício pede para você
        colocar algumas mensagens importantes, 'usuário começa', 'computador
        começa' e 'usuário venceu', ou o 'computador venceu'. Essas mensagens
        o corretor vai usar para saber se o jogo aconteceu de acordo com o
        esperado, ou seja, se quem tinha que começar começou, se quem ganhou
        de fato era quem era esperado ganhar. Então esses são os detalhes que
        as pessoas normalmente esquecem. Vamos ver se você com essas dicas
        aqui consegue matar esse programa com facilidade.







def computador_escolhe_jogada(X, Y):

    return(0)

# interio correspondente à próxima jodada do computador de acordo com a estratégia vencedora


def usuario_escolhe_jogada(X, Y):
    removidas = int(input("Quantas peças você vai tirar? "))

    while(pecas > m):
        print("Oops! Jogada inválida! Tente de novo.")
        removidas = int(input("Quantas peças você vai tirar? "))

    return(removidas)

def partida():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    n = int(input("Quantas peças? ")
    m = int(input("Limite de peças por jogada? ")

    if((n % (m + 1)) == 0):
        print("Você começa")
        i = 0

    else:
        print("Computador começa")
        i = 1

    while(n =! 0):
        if(i == 0)
            

def campeonato():
    i = 0
    while(i < 3):
        partida()



