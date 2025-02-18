

def caixa():
    x = 'false'
    r = 0
    print('\033[1;33;40m{:-^60}\033[m'.format('Caixa'))
    print('[1]Preços\n[2]Comprar produtos\n[3]Comprar Móveis\n[4]Almentar loja\n[5]Voltar')
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5':
            x = 'true'
    if r == '1':
        x = 'false'
        r = 0
        print('[1]Ver preços\n[2]Alterar preços\n[3]Ver preço médio de mercado\n[4]Voltar')
        while x != 'true':
            r = input('').strip()
            if r == '1' or r == '2' or r == '3' or r == '4':
                x = 'true'
        if r == '1':
            from dados_game import p, q
            produtos = ['Maçã', 'Pêra', 'Banana', 'Tomate', 'Alface', 'Batata', 'C.Cola2L']
            unidades = ['kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'frd']

            print('| Produto | Preço geral | Quantia | Preço unidade')
            for i in range(len(produtos)):
                preco_unidade = p[i] / q[i]
                print('|{:^9}|{:^13}|{:^9}|{:^15.2f}'.format(produtos[i], '{}/{}'.format(p[i], unidades[i]), q[i],
                                                             preco_unidade))
            x = input('Voltar = enter')
            caixa()
        elif r == '2':
            alterarpreco()
        elif r == '3':
            produtos = ['Maçã', 'Pêra', 'Banana', 'Tomate', 'Alface', 'Batata', 'C.Cola2L']
            unidades = ['kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'frd']
            from dados_game import l_precos
            print('| Produto | Média de mercado |')
            for c in range(0, 7):
                print('|{:^9}|{:^18}|'.format(produtos[c], '{}/{}'.format(l_precos[c], unidades[c])))
        elif r == '4':
            from gamefiles import jogo_tl_i
            jogo_tl_i.painelinicial()
    elif r == '5':
        from gamefiles import jogo_tl_i
        jogo_tl_i.painelinicial()


def alterarpreco():
    from dados_game import p
    from time import sleep
    print('Qual preço deseja alterar ?\n[1]Maçã : {}/kg\n[2]Pêra : {}/kg\n[3]Banana : {}/kg\n[4]Tomate : {}/kg\
    \n[5]Alface : {}/kg\n[6]Batata : {}/kg\n[7]C.Cola2L : {}/frd\n[8]Voltar'
          .format(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
    r = input('').strip()
    if r == '1':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[0] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '2':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[1] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '3':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[2] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '4':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[3] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '5':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[4] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '6':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[5] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '7':
        while True:  # Loop para validar a entrada
            try:
                x = float(input('Digite o novo valor: '))
                if x > 0:  # Verifica se o valor é positivo
                    p[6] = x
                    salvar_dados(p)
                    break  # Sai do loop se a entrada for válida
                else:
                    print("O valor do preço deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    elif r == '8':
        caixa()
    else:
        print('ERRO')
        sleep(2)
        caixa()
    sleep(1)
    print('Valor atualizado !')
    sleep(1)
    r = input('[1]Alterar outros preços\n[2]Voltar ao caixa')
    if r == '1':
        alterarpreco()
    else:
        caixa()


def salvar_dados(p):
    # Lê o conteúdo atual do arquivo 'dados_game.py'
    with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
        linhas = arquivo.readlines()
    # Abre o arquivo 'dados_game.py' em modo de escrita
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            # Atualiza a linha que contém a lista 'p'
            if linha.startswith('p ='):
                arquivo.write("p = [{}]\n".format(', '.join(map(str, p))))  # Salva a lista 'p' atualizada
            else:
                arquivo.write(linha)  # Mantém as outras linhas inalteradas

