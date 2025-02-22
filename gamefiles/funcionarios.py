from time import sleep


def diarista():
    from dados_game import dinheiro
    if dinheiro >= 100:
        # Lê o conteúdo atual do arquivo 'dados_game.py'
        with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
            linhas = arquivo.readlines()
        # Abre o arquivo 'dados_game.py' em modo de escrita
        with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
            for linha in linhas:
                # zerar a sujeira
                if linha.startswith('sujeira ='):
                    arquivo.write("sujeira = 0")
                elif linha.startswith('dinheiro = '):
                    arquivo.write("dinheiro = {}".format(dinheiro - 100))
                else:
                    arquivo.write(linha)  # Mantém as outras linhas inalteradas
        sleep(2)
        print('Limpeza concluída !')
        sleep(2)
    else:
        print('Dinheiro insuficiente !')
        sleep(2)

