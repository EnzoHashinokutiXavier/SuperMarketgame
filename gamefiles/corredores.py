from gamefiles import jogo_tl_i
from time import sleep


def corredores():
    print('\033[1;33;40m{:-^60}\033[m'.format('Corredores'))
    print('[1]Ver corredores\n[2]Mover prateleiras\n[3]Examinar sujeira\n[4]Voltar')
    x = 'false'
    r = 0
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5':
            x = 'true'

    if r == '1':
        from dados_game import aresp, artipo, arproduto, arquant, aresp2, artipo2, arproduto2, arquant2
        i = -1
        print('| Fileira1 | Produto  | Quantia  |    | Fileira2 | Produto  | Quantia  |')
        while True:
            i += 1
            if i == 8:
                break
            if aresp[i] == aresp2[i] == 'liberado':
                print('|{:^10}|{:^10}|{:^10}|    |{:^10}|{:^10}|{:^10}|'.format(artipo[i], arproduto[i], arquant[i],
                                                                                artipo2[i], arproduto2[i], arquant2[i]))
            elif aresp[i] == 'liberado' and aresp2[i] == 'bloqueado':
                print('|{:^10}|{:^10}|{:^10}|'.format(artipo[i], arproduto[i], arquant[i]))
        x = input('Voltar = enter')
        corredores()
    elif r == '2':
        from dados_game import aresp, artipo, arproduto, arquant, aresp2, artipo2, arproduto2, arquant2
        i = -1
        n = -1
        c = 0
        print('  | Fileira1 | Produto  |    | Fileira2 | Poduto  |')
        while True:
            i += 1
            n += 2
            if i == 8:
                break
            if aresp[i] == aresp2[i] == 'liberado':
                print('{:^2}|{:^10}|{:^10}|  {:^2}|{:^10}|{:^10}|'.format(n, artipo[i], arproduto[i], n+1,
                                                                          artipo2[i], arproduto2[i]))
                c = 1
            elif aresp[i] == 'liberado' and aresp2[i] == 'bloqueado':
                print('{:^2}|{:^10}|{:^10}|'.format(n, artipo[i], arproduto[i]))
                c = 2
        print('Qual prateleira / freezer deseja mover ?')
        while True:
            try:
                a = int(input(''))
                if c == 1:
                    if 0 < a < (n + 1):
                        break
                if c == 2:
                    if 0 < a < n:
                        break
                if c == 0:
                    print('Erro codigo 1, voltando aos corredores')
                    sleep(2)
                    corredores()
            except ValueError:
                print("Por favor, digite um número válido.")
        if a % 2 != 0:
            d = a // 2
            copiaesp1 = aresp[d]
            copiatipo1 = artipo[d]
            copiaproduto1 = arproduto[d]
            copiaquant1 = arquant[d]
        elif a % 2 == 0:
            d = (a/2) - 1
            copiaesp1 = aresp2[d]
            copiatipo1 = artipo2[d]
            copiaproduto1 = arproduto2[d]
            copiaquant1 = arquant2[d]
        print('Para qual espaço será movido ?')
        while True:
            try:
                b = int(input(''))
                if c == 1:
                    if 0 < b < (n + 1):
                        break
                if c == 2:
                    if 0 < b < n:
                        break
                if c == 0:
                    print('Erro codigo 1, voltando aos corredores')
                    sleep(2)
                    corredores()
            except ValueError:
                print("Por favor, digite um número válido.")
        if b % 2 != 0:
            e = b // 2
            copiaesp2 = aresp[e]
            copiatipo2 = artipo[e]
            copiaproduto2 = arproduto[e]
            copiaquant2 = arquant[e]
        elif b % 2 == 0:
            e = (b / 2) - 1
            copiaesp2 = aresp2[e]
            copiatipo2 = artipo2[e]
            copiaproduto2 = arproduto2[e]
            copiaquant2 = arquant2[e]
        #Inverta os valores e faça um sistema de salvamento ---------

        sleep(2)
        print('Mudança realizada !')
        corredores()
    elif r == '3':
        from dados_game import sujeira
        if sujeira == 0:
            print('O chão está limpo !')
            sleep(2)
            corredores()
        elif sujeira in [1, 2]:
            print('Os corredores estão com pouca sujeira !')
        elif sujeira >= 3:
            print('Os corredores estão sujos !')
        print('[1]Contratar Diarista : R$100.00\n[2]Contratar funcionário por 30 dias : R$1600.00\n[3]Deixar assim mesm\
o')
        x = 'false'
        r = 0
        while x != 'true':
            r = input('').strip()
            if r == '1' or r == '2' or r == '3':
                x = 'true'
        if r == '1':
            from funcionarios import diarista
            diarista()
            corredores()
        elif r == '2':
            from dados_game import dinheiro, funcionario_limpeza
            if dinheiro >= 1600:
                with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
                    linhas = arquivo.readlines()
                # Abre o arquivo 'dados_game.py' em modo de escrita
                with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
                    for linha in linhas:
                        # zerar a sujeira
                        if linha.startswith('funcionario_limpeza ='):
                            arquivo.write("funcionario_limpeza = {}\n".format(funcionario_limpeza + 30))
                        elif linha.startswith('dinheiro = '):
                            arquivo.write("dinheiro = {}\n".format(dinheiro - 1600))
                        else:
                            arquivo.write(linha)  # Mantém as outras linhas inalteradas
            else:
                print('Saldo insuficiente !')
            sleep(2)
            corredores()
        elif r == '3':
            corredores()
    elif r == '4':
        jogo_tl_i.painelinicial()


def salvar_dados(ar):
    # Lê o conteúdo atual do arquivo 'dados_game.py'
    with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
        linhas = arquivo.readlines()
    # Abre o arquivo 'dados_game.py' em modo de escrita
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            # Atualiza a linha que contém a lista 'p'
            if linha.startswith('ar ='):
                arquivo.write("ar = [{}]\n".format(', '.join(map(str, ar))))  # Salva a lista 'p' atualizada
            else:
                arquivo.write(linha)  # Mantém as outras linhas inalteradas

