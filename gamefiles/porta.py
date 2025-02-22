from gamefiles import jogo_tl_i, salvar_jogo


def porta():
    x = 'false'
    r = 0
    print('\033[1;33;40m{:-^60}\033[m'.format('Porta'))
    print('[1]Abrir loja\n[2]Encomendas\n[3]Salvar e sair\n[4]Voltar')
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5':
            x = 'true'
    if r == '1':
        print('loja aberta')
    elif r == '2':
        from dados_game import encomendas, entrega
        y = 0
        print('Encomendas disponíveis para retirada :')
        i = -1
        n = 0
        while True:
            i += 1
            if i == 8:
                break
            if encomendas[i] != 'vazio' and entrega[i] == 0:
                n += 1
                y = 1
                print('{}| {}'.format(n, encomendas[i]))
        if y == 0:
            print('Não há entregas prontas para serem retiradas !')
        print('Encomendas em transporte :\nEncomendas | Dias p/ entrega')
        z = 0
        i = -1
        while True:
            i += 1
            if i == 8:
                break
            if encomendas[i] != 'vazio' and entrega[i] > 0:
                print('{:^10} |{:^10}'.format(encomendas[i], entrega[i]))
                z = 1
        if z == 0:
            print('Não há encomendas a caminho !')
        if y == 0:
            x = input('Voltar = enter')
            porta()
        print('Deseja retirar alguma encomenda ?\n[1]Retirar encomenda\n[2]Voltar')
        while True:
            r = input('')
            if r == '1' or r == '2':
                break
        if r == '1':
            from dados_game import estoque_livre
            from time import sleep
            if estoque_livre == 0:
                print('Não há espaço no estoque')
                sleep(2)
                porta()

            def retirar_encomenda():
                from dados_game import estoque, estoque_livre, estoque_limite, quant_encomendas_disponiveis
                print("Qual encomenda deseja retirar ?")
                while True:
                    try:
                        e = int(input(''))
                        if n >= e > 0:
                            break
                    except ValueError:
                        print("Por favor, digite um número válido.")
                a = -1
                b = 0
                while True:
                    a += 1
                    if encomendas[a] != 'vazio' and entrega[a] == 0:
                        b += 1
                    if b == e:
                        break
                c = -1
                while True:
                    c += 1
                    if c == estoque_limite:
                        print('Limite de estoque atingido : erro')
                    if estoque[c] == 'vazio':
                        estoque[c] = encomendas[a]
                        break
                estoque_livre -= 1
                encomendas[a] = 'vazio'
                quant_encomendas_disponiveis += 1
                salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                print('{} foi adicionado ao estoque !'.format(estoque[c]))
                sleep(2)
                d = input('[1]Retirar mais produtos\n[2]Voltar\n')
                if d == '1':
                    retirar_encomenda()
                elif d == '2':
                    porta()
                else:
                    print('Erro, voltando a porta !')
                    sleep(2)
                    porta()
            retirar_encomenda()
        elif r == '2':
            porta()
    elif r == '3':
        salvar_jogo.savegame()
    elif r == '4':
        jogo_tl_i.painelinicial()


def salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis):
    with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
        linhas = arquivo.readlines()
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            if linha.startswith('quant_encomendas_disponiveis ='):
                arquivo.write("quant_encomendas_disponiveis = {}\n".format(quant_encomendas_disponiveis))
            elif linha.startswith('estoque_livre ='):
                arquivo.write("estoque_livre = {}\n".format(estoque_livre))
            elif linha.startswith('encomendas ='):
                arquivo.write("encomendas = ['{}']\n".format(', '.join(map(str, encomendas))))
            elif linha.startswith('estoque ='):
                arquivo.write("estoque = [{}]\n".format(', '.join(map(str, estoque))))
            else:
                arquivo.write(linha)
