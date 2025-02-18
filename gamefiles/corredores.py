

def corredores():
    print('\033[1;33;40m{:-^60}\033[m'.format('Corredores'))
    print('[1]Ver corredores\n[2]Mover prateleiras\n[3]Organizar produtos\n[4]Preços\n[5]Voltar')
    x = 'false'
    r = 0
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5':
            x = 'true'
    if r == '1':
        from dados_game import ar
        print('  |  Espaço  |   Tipo   |  Produto |  Quantia ')
        for i in range(0, len(ar), 4):  # Iteramos de 4 em 4
            print(f'{i // 4 + 1:02}|{ar[i]:^10}|{ar[i + 1]:^10}|{ar[i + 2]:^10}|{ar[i + 3]:^10}')
        x = input('Voltar = enter')
        corredores()



