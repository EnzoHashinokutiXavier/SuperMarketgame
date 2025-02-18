import sys

import dados_game
from gamefiles import porta
from time import sleep


def savegame():
    from dados_save1 import slot1
    from dados_save2 import slot2
    from dados_save3 import slot3
    from dados_save4 import slot4
    print('\033[1;33;40m{:-^60}\033[m'.format('Escolha o slot de salvamento'))
    print('[1]Salvamento {}\n[2]Salvamento {}\n[3]Salvamento {}\n[4]Salvamento {}\n[5]Voltar\n'
          .format(slot1[0], slot2[0], slot3[0], slot4[0]))
    x = False
    r = ''
    while not x:
        r = input('').strip()
        if r in ['1', '2', '3', '4', '5']:
            x = True
    if r == '1':
        salvar_dados(1, dados_game.nome)
    elif r == '2':
        salvar_dados(2, dados_game.nome)
    elif r == '3':
        salvar_dados(3, dados_game.nome)
    elif r == '4':
        salvar_dados(4, dados_game.nome)
    elif r == '5':
        porta.porta()
    print('Salvando dados')
    for c in range(0, 3):
        sleep(1)
        print('.')
    print('Dados Salvos !')
    sleep(2)
    sys.exit()


def salvar_dados(slot, nome):
    with open('../SuperMarketGame/dados_game.py', 'r') as leitura:
        conteudo = leitura.read()
    if f'slot{slot} = [\'de {nome}\']' not in conteudo:
        with open(f'dados_save{slot}.py', 'w') as arquivo:
            arquivo.write(f'slot{slot} = [\'de {nome}\']\n')
            arquivo.write(conteudo)
    else:
        with open(f'dados_save{slot}.py', 'w') as arquivo:
            arquivo.write(conteudo)


