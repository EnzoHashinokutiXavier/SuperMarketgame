def passardia():
    from dados_game import dia
    import precorandom
    dia += 1
    with open('../SuperMarketGame/dados_game.py', 'r') as ler:
        linhas = ler.readlines()
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            if linha.startswith('dia'):
                arquivo.write('dia = {}'.format(dia))
            else:
                arquivo.write(linha)
    precorandom.precorandom()
    