import random


def precorandom():
    from dados_game import l_precos
    for c in range(0, 7):
        maisoumenos = random.random()
        quantia = random.randint(1, 10)
        if maisoumenos == 0:
            l_precos[c] += l_precos[c] * (quantia / 100)
        elif maisoumenos == 1:
            l_precos[c] = l_precos[c] - (l_precos[c] * (quantia / 100))
        savel(l_precos)


def savel(l_precos):
    with open('../SuperMarketGame/dados_game.py', 'r') as ler:
        linhas = ler.readlines()
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            if linha.startswith('l_precos'):
                arquivo.write('l_precos = [{}]'.format(', '.join(map(str, l_precos))))
            else:
                arquivo.write(linha)

