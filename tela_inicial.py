import sys

import tutorial
from gamefiles import jogo_tl_i
import os


def telainicial():
    print('[1]Novo jogo\n[2]Carregar salvamento\n[3]Créditos\n[4]Sair\n')
    ti_opc = ''
    x = False
    while not x:
        ti_opc = input('').strip()
        if ti_opc in ['1', '2', '3', '4']:
            x = True
    if ti_opc == '1':
        print('Deseja jogar o tutorial ?\n[1]Jogar tutorial\n[2]Pular tutorial\n[3]Voltar\n')
        x = False
        nj_opc = ''
        while not x:
            nj_opc = input('').strip()
            if nj_opc in ['1', '2', '3', '4', '5']:
                x = True
        if nj_opc == '1':
            with open('dadosiniciais.py', 'r') as ler:
                dados = ler.read()
            with open('dados_game.py', 'w', buffering=1) as criar:
                criar.write(dados)
                os.fsync(criar.fileno())
            tutorial.tutorial_inicio()
        elif nj_opc == '2':
            nome = input('Digite seu nome:').strip()
            with open('dadosiniciais.py', 'r') as ler:
                dados = ler.read()
            with open('dados_game.py', 'w') as criar:
                criar.write(str("nome = '{}'\n{}".format(nome, dados)))
                os.fsync(criar.fileno())
            jogo_tl_i.painelinicial()
        elif nj_opc == '3':
            telainicial()
    elif ti_opc == '2':
        from dados_save1 import slot1
        from dados_save2 import slot2
        from dados_save3 import slot3
        from dados_save4 import slot4

        slots = [slot1, slot2, slot3, slot4]
        slot_names = ['dados_save1.py', 'dados_save2.py', 'dados_save3.py', 'dados_save4.py']

        def carregar_dados(slot_index):
            if slots[slot_index][0] == 'vazio':
                telainicial()
            else:
                with open(slot_names[slot_index], 'r') as ler:
                    conteudo = ler.read()
                with open('dados_game.py', 'w') as criar:
                    criar.write(conteudo)
                    os.fsync(criar.fileno())

        print('[1]Salvamento {}\n[2]Salvamento {}\n[3]Salvamento {}\n[4]Salvamento {}\n[5]Voltar\n'
              .format(slot1[0], slot2[0], slot3[0], slot4[0]))
        x = False
        cj_opc = ''
        while not x:
            cj_opc = input('').strip()
            if cj_opc in ['1', '2', '3', '4', '5']:
                x = True

        if cj_opc in ['1', '2', '3', '4']:
            carregar_dados(int(cj_opc) - 1)
        elif cj_opc == '5':
            telainicial()
        jogo_tl_i.painelinicial()
    elif ti_opc == '3':
        with open('créditos.txt', 'r') as ler:
            conteudo = ler.read()
            print(conteudo)
        x = input('Voltar = enter')
        telainicial()
    elif ti_opc == '4':
        sys.exit()

