

def painelinicial():
    from gamefiles import caixa, estoque, corredores, porta
    from dadosiniciais import dia
    print('\033[1;33;40m{:-^60}\033[m'.format('Loja--Dia-{}'.format(dia)))
    print('[1]Ir a porta\n[2]Ir aos corredores\n[3]Ir ao estoque\n[4]Ir ao caixa')
    x = 'false'
    r = 0
    while x != 'true':
        r = input('').strip()
        if r == '1' or r == '2' or r == '3' or r == '4':
            x = 'true'
    if r == '1':
        porta.porta()
    elif r == '2':
        corredores.corredores()
    elif r == '3':
        estoque.estoque()
    elif r == '4':
        caixa.caixa()


