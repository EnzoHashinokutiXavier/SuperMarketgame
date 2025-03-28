from time import sleep
from jogo_tl_i import painelinicial


def estoque():
    from dados_game import estoque_limite, estoque_livre, estoque
    print('\033[1;33;40m{:-^60}\033[m'.format('Estoque'))
    print('[1]Ver itens em estoque\n[2]Levar itens aos corredores\n[3]Descartar item\n[4]Voltar')
    while True:
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4':
            break
    if r == '1':
        if estoque_livre == estoque_limite:
            print('Não há itens no estoque !')
            sleep(2)
            estoque()
        print(' | Produtos')
        for c in range(0, estoque_limite):
            print('{:^2}|{}'.format((c + 1), estoque[c]))
        x = input("Voltar = enter")
        estoque()
    elif r == '2':
        from dados_game import (aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2, nomes_comida,
                                nomes_bebidas, quantia_comida, quantia_bebidas, encomendas, quant_encomendas_disponiveis)
        from corredores import salvar_dados
        from porta import salvar_retirada
        if estoque_livre == estoque_limite:
            print('Não há itens no estoque !')
            sleep(2)
            estoque()
        print(' | Produtos')
        a = 0
        for c in range(0, estoque_limite):
            if estoque[c] != 'vazio':
                a += 1
                print('{:^2}|{}'.format(a, estoque[c]))
        print('Qual produto deseja retirar ?')
        while True:
            try:
                r = int(input(''))     #produto do estoque na contagem dos que nao sao vazio
                if 0 < r <= a:
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
        b = -1
        d = 0
        while True:
            b += 1
            if estoque[b] != 'vazio':
                d += 1
                if d == r:
                    nome = estoque[b]               #recebe nome do item
                    estoque[b] = str('vazio')       #apaga item do estoque (salve o estoque depois)
                    break
        # Se for movel
        if nome in ['prateleira', 'freezer']:       # Se for Estande ou freezer
            for c in range(0, 9):
                if aresp[c] == 'liberado' and artipo[c] == 'vazio':
                    artipo[c] = nome                #coloca item (salve artipo depois)
                    print('Item adicionado aos corredores !')
                    estoque_livre += 1              #(salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
                if aresp2[c] == 'liberado' and artipo2[c] == 'vazio':
                    artipo2[c] = nome               #coloca item (salve artipo depois)
                    print('Item adicionado aos corredores !')
                    estoque_livre += 1              # (salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
            print('Nenhum espaço livre encontrado, aumente sua loja !')
            sleep(2)
            estoque()
        # Se for comida
        elif nome in nomes_comida:
            numero = nomes_comida.index(nome)
            for i in range(0, 9):
                if artipo[i] == 'prateleira' and arproduto == 'vazio':
                    arproduto[i] = nomes_comida[numero]          #(salvar arproduto)
                    arquant[i] = quantia_comida[numero]          #(salvar quantia)
                    print('Alimento adicionado a prateleira !')
                    estoque_livre += 1  # (salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
                if artipo2[i] == 'prateleira' and arproduto == 'vazio':
                    arproduto2[i] = nomes_comida[numero]          #(salvar arproduto)
                    arquant2[i] = quantia_comida[numero]          #(salvar quantia)
                    print('Alimento adicionado a prateleira !')
                    estoque_livre += 1  # (salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
            print('Nenhum espaço livre encontrado, compre uma prateleira !')
            sleep(2)
            estoque()
        # Se for bebida
        elif nome in nomes_bebidas:
            numero = nomes_bebidas.index(nome)
            for i in range(0, 9):
                if artipo[i] == 'freezer' and arproduto == 'vazio':
                    arproduto[i] = nomes_bebidas[numero]  # (salvar arproduto)
                    arquant[i] = quantia_bebidas[numero]  # (salvar quantia)
                    print('Bebida adicionada ao freezer !')
                    estoque_livre += 1  # (salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
                if artipo2[i] == 'freezer' and arproduto == 'vazio':
                    arproduto2[i] = nomes_bebidas[numero]  # (salvar arproduto)
                    arquant2[i] = quantia_bebidas[numero]  # (salvar quantia)
                    print('Bebida adicionada ao freezer !')
                    estoque_livre += 1  # (salvar estoquelivre)
                    salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
                    salvar_retirada(estoque, estoque_livre, encomendas, quant_encomendas_disponiveis)
                    sleep(2)
                    estoque()
            print('Nenhum espaço livre encontrado, compre um freezer !')
            sleep(2)
            estoque()





            


    elif r == '3':
        if estoque_livre == estoque_limite:
            print('Não há itens no estoque !')
            sleep(2)
            estoque()
        #fazer sistema

    elif r == '4':
        painelinicial()



    