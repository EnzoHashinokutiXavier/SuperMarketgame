import sys

import dados_save1
import dados_save2
import dados_save3
import dados_save4
import game
import situacaosave
import tutorial


def telainicial():
    ti_opc = input('[1]Novo jogo\n[2]Carregar salvamento\n[3]Créditos\n[4]Sair\n').strip()
    if ti_opc == '1':
        nj_opc = input('Deseja jogar o tutorial ?\n[1]Jogar tutorial\n[2]Pular tutorial\n[3]Voltar\n').strip()
        if nj_opc == '1':
            tutorial.tutorial_inicio()
        elif nj_opc == '2':
            game.startgame()
        elif nj_opc == '3':
            telainicial()
        else:
            ti_erro()
    elif ti_opc == '2':
        from situacaosave import lista
        situacaosave.listanv()
        cj_opc = input('[1]Salvamento {}\n[2]Salvamento {}\n[3]Salvamento {}\n[4]Salvamento {}\n'
                       .format(lista[0], lista[1], lista[2], lista[3])).strip()
        if cj_opc == '1':
            dados_save1.loadsave()
        elif cj_opc == '2':
            dados_save2.loadsave()
        elif cj_opc == '3':
            dados_save3.loadsave()
        elif cj_opc == '4':
            dados_save4.loadsave()
        else:
            ti_erro()
        game.startgame()
    elif ti_opc == '3':
        with open('créditos.txt', 'r') as arq:
            ler = arq.read()
            print(ler)
            x = input('\nVoltar ao menu principal = enter')
            telainicial()
    elif ti_opc == '4':
        sys.exit()
    else:
        ti_erro()


def ti_erro():
    print('\033[1;33;40m{:-^60}\033[m'.format('Escolha uma das opções disponíveis !'))
    telainicial()
