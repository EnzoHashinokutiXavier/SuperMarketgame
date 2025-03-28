from gamefiles import jogo_tl_i
from time import sleep


def corredores():
    print('\033[1;33;40m{:-^60}\033[m'.format('Corredores'))
    print('[1]Ver corredores\n[2]Mover prateleiras\n[3]Examinar sujeira\n[4]Mover prateleira ao estoque\n[5]Voltar')
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
            d = int(a // 2)
            copiaesp1 = str(aresp[d])
            copiatipo1 = str(artipo[d])
            copiaproduto1 = str(arproduto[d])
            copiaquant1 = int(arquant[d])
        elif a % 2 == 0:
            d = int((a//2) - 1)
            copiaesp1 = str(aresp2[d])
            copiatipo1 = str(artipo2[d])
            copiaproduto1 = str(arproduto2[d])
            copiaquant1 = int(arquant2[d])
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
            e = int(b // 2)
            copiaesp2 = str(aresp[e])
            copiatipo2 = str(artipo[e])
            copiaproduto2 = str(arproduto[e])
            copiaquant2 = int(arquant[e])
        elif b % 2 == 0:
            e = int((b // 2) - 1)
            copiaesp2 = str(aresp2[e])
            copiatipo2 = str(artipo2[e])
            copiaproduto2 = str(arproduto2[e])
            copiaquant2 = int(arquant2[e])
        #inverte os valores e salva
        if a % 2 != 0:
            d = a // 2
            aresp[d] = str(copiaesp2)
            artipo[d] = str(copiatipo2)
            arproduto[d] = str(copiaproduto2)
            arquant[d] = int(copiaquant2)
        elif a % 2 == 0:
            d = (a//2) - 1
            aresp2[d] = str(copiaesp2)
            artipo2[d] = str(copiatipo2)
            arproduto2[d] = str(copiaproduto2)
            arquant2[d] = int(copiaquant2)
        if b % 2 != 0:
            e = b // 2
            aresp[e] = str(copiaesp1)
            artipo[e] = str(copiatipo1)
            arproduto[e] = str(copiaproduto1)
            arquant[e] = int(copiaquant1)
        elif b % 2 == 0:
            e = (b // 2) - 1
            aresp2[e] = str(copiaesp1)
            artipo2[e] = str(copiatipo1)
            arproduto2[e] = str(copiaproduto1)
            arquant2[e] = int(copiaquant1)
        salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2)
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
    elif r == '5':
        jogo_tl_i.painelinicial()


def salvar_dados(aresp, aresp2, artipo, artipo2, arproduto, arproduto2, arquant, arquant2):
    # Lê o conteúdo atual do arquivo 'dados_game.py'
    with open('../SuperMarketGame/dados_game.py', 'r') as arquivo:
        linhas = arquivo.readlines()
    # Abre o arquivo 'dados_game.py' em modo de escrita
    with open('../SuperMarketGame/dados_game.py', 'w') as arquivo:
        for linha in linhas:
            if linha.startswith('aresp ='):
                arquivo.write("aresp = {}\n".format(aresp))  # Sem join
            elif linha.startswith('artipo ='):
                arquivo.write("artipo = {}\n".format(artipo))  # Sem join
            elif linha.startswith('arproduto ='):
                arquivo.write("arproduto = {}\n".format(arproduto))  # Sem join
            elif linha.startswith('arquant ='):
                arquivo.write("arquant = {}\n".format(arquant))  # Sem join
            elif linha.startswith('aresp2 ='):
                arquivo.write("aresp2 = {}\n".format(aresp2))  # Sem join
            elif linha.startswith('artipo2 ='):
                arquivo.write("artipo2 = {}\n".format(artipo2))  # Sem join
            elif linha.startswith('arproduto2 ='):
                arquivo.write("arproduto2 = {}\n".format(arproduto2))  # Sem join
            elif linha.startswith('arquant2 ='):
                arquivo.write("arquant2 = {}\n".format(arquant2))  # Sem join
            else:
                arquivo.write(linha)  # Mantém as outras linhas inalteradas

