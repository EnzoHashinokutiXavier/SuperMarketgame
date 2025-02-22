import jogo_tl_i


def passardia():
    from dados_game import dia, funcionario_limpeza, sujeira
    import precorandom
    dia += 1
    if funcionario_limpeza >= 1:
        funcionario_limpeza -= 1
        sujeira = 0
    with open('../SuperMarketGame/dados_game.py', 'r') as ler:
        linhas = ler.readlines()
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            if linha.startswith('dia'):
                arquivo.write('dia = {}'.format(dia))
            elif linha.startswith('funcionario_limpeza ='):
                arquivo.write("funcionario_limpeza = {}".format(funcionario_limpeza))
            elif linha.startswith('sujeira ='):
                arquivo.write("sujeira = {}".format(sujeira))
            else:
                arquivo.write(linha)
    precorandom.precorandom()
    jogo_tl_i.painelinicial()
