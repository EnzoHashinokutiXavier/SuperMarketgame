from gamefiles import jogo_tl_i, salvar_jogo


def porta():
    x = 'false'
    r = 0
    print('\033[1;33;40m{:-^60}\033[m'.format('Porta'))
    print('[1]Abrir loja\n[2]Receber encomendas\n[3]Salvar e sair\n[4]Voltar')
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5':
            x = 'true'
    if r == '1':
        print('loja aberta')
    elif r == '2':
        print('Encomendas recebidas')
    elif r == '3':
        salvar_jogo.savegame()
    elif r == '4':
        jogo_tl_i.painelinicial()

