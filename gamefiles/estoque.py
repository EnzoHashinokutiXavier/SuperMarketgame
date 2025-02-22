from time import sleep


def estoque():
    print('voce esta no estoque')


def colocar_movel():
    from dados_game import ar
    x = 0
    print('    |  Espaço  |   Tipo   |')
    for i in range(0, len(ar), 4):  # Iteramos de 4 em 4
        if (ar[i]) == 'liberado' and (ar[i + 1]) == 'vazio':
            print(f'[{i // 4 + 1:02}]|{ar[i]:^10}|{ar[i + 1]:^10}|')
            x = 1
        else:
            continue
    if x == 0:
        print('Não há espaços livres !')
        sleep(2)
        estoque()
    print('Em qual espaço será colocado o novo móvel')
    while True:
        e = int(input(''))
        indice = (e - 1) * 4
        if ar[indice] == 'liberado':
            break