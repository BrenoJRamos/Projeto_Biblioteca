
catalogo = []
livro = {}


def menu():
    print('|', '-='*13, '|')
    print('|', 'BIBLIOTECA'.center(25), ' |')
    print('|', '-='*13, '|')
    while True:
        print('')
        print('para sair [\033[1;32msair\033[m]')
        print('Para adicionar [\033[1;32madicionar\033[m], para remover [\033[1;32mremover\033[m] e para '
              'filtrar [\033[1;32mfiltrar\033[m]')
        esc1 = str(input('\033[1mDeseja remover, adicionar ou filtrar livros? : \033[m')).lower().strip()
        print('')
        while esc1 != 'remover' and esc1 != 'adicionar' and esc1 != 'sair' and esc1 != 'filtrar':
            esc1 = str(input('\033[1mDigite corretamente!: \033[m')).lower().strip()
        if esc1 == 'sair':
            break
        else:
            if len(catalogo) == 0 and esc1 != 'adicionar':
                print('\033[1;31mAdicione um livro na biblioteca primeiro!!\033[m')
            else:
                if esc1 == 'adicionar':
                    criarLivro(livro)
                elif esc1 == 'filtrar':
                    filtrarLivros(catalogo)
                else:
                    listarLivros(catalogo)
                    removerLivro(catalogo)
    if len(catalogo) == 0:
        print('\033[1;34mVocê não adicionou livros!!\033[m')
    else:
        listarLivros(catalogo)
    print('\033[1mVolte sempre!\033[m \033[1;34m^^\033[m')


def criarLivro(livro):
    print('para sair [\033[1;32msair\033[m]')
    while True:
        titulo = str(input('\033[1mDigite o título do livro: \033[m')).strip()
        if titulo == 'sair':
            break
        livro['Título'] = titulo
        nome = str(input('\033[1mDigite o nome do autor: \033[m')).strip()
        livro['Autor'] = nome
        gen = str(input('\033[1mDigite o gênero: \033[m')).strip()
        livro['Gênero'] = gen
        while True:
            try:
                qt = int(input('\033[1mDigite a quantidade de livros: \033[m'))
            except ValueError:
                print('\033[1;31mOps! Valor inválido\033[m')
            else:
                break
        livro['Quantidade'] = qt
        catalogo.append(livro.copy())
        livro.clear()
        print('')
        print('\033[1m[\033[1;32ms\033[m] para Sim e [\033[1;32mn\033[m] para Não\033[m')
        esc = str(input('\033[1mDeseja adicionar mais livros?: \033[m')).upper().strip()
        print('')
        while esc != 'N' and esc != 'S':
            esc = str(input('\033[1mDigite corretamente \033[1;32mS\033m [Sim] e  \033[1;32mN\033[m [Não]: \033[m')).upper().strip()
        if esc == 'S':
            continue
        else:
            listarLivros(catalogo)
            break

def removerLivro(catalogo):
    while True:
        print('para sair [\033[1;32msair\033[m]')
        remove = str(input('\033[1mDigite o nome do livro que você quer remover: \033[m')).strip().lower()
        if remove == 'sair':
            break
        remove1 = str(input('\033[1mDigite o autor do livro que você quer remover: \033[m')).strip().lower()
        livro_encontrado = False

        for c in range(len(catalogo) - 1, -1, -1):
            if remove == catalogo[c]['Título'].lower() and remove1 == catalogo[c]['Autor'].lower():
                print(f"\033[1;34m{catalogo[c]['Título']}\033[m \033[1mfoi removido com sucesso\033[m")
                del catalogo[c]
                livro_encontrado = True

        if not livro_encontrado:
            print('\033[1;31mEsse livro não existe!!\033[m')
        print('\033[1m[\033[1;32ms\033[m] para Sim e [\033[1;32mn\033[m] para Não\033[m')
        esc3 = str(input('\033[1mDeseja remover mais livros?: \033[m')).upper().strip()
        print('')
        while esc3 != 'N' and esc3 != 'S':
            esc3 = str(input('\033[1mDigite corretamente \033[1;32mS\033[m [Sim] e  \033[1;32mN\033[m [Não]: \033[m')).upper().strip()
        if esc3 == 'S':
            continue
        else:
            break


def listarLivros(catalogo):
    print('-=' * 20)
    print('CATÁLOGO'.center(40))
    for c in range(0, len(catalogo)):
        print('-=' * 20)
        print(f'\033[1mLIVRO {c + 1}\033[m')
        print(f"\033[1;35mTítulo do livro:\033[m \033[1;33m{catalogo[c]['Título'].capitalize()}\033[m")
        print(f"\033[1;35mAutor do livro:\033[m \033[1;33m{catalogo[c]['Autor'].capitalize()}\033[m")
        print(f"\033[1;35mQuantidade de livros:\033[m \033[1;33m{catalogo[c]['Quantidade']}\033[m")
        print(f"\033[1;35mGênero do livro:\033[m \033[1;33m{catalogo[c]['Gênero'].capitalize()}\033[m")
        print('-=' * 20)


def listarFiltro(c, catalogo):
    print('-=' * 20)
    print(f'\033[1mLIVRO {c + 1}\033[m')
    print(f"\033[1;35mTítulo do livro:\033[m \033[1;33m{catalogo[c]['Título'].capitalize()}\033[m")
    print(f"\033[1;35mAutor do livro:\033[m \033[1;33m{catalogo[c]['Autor'].capitalize()}\033[m")
    print(f"\033[1;35mQuantidade de livros:\033[m \033[1;33m{catalogo[c]['Quantidade']}\033[m")
    print(f"\033[1;35mGênero do livro:\033[m \033[1;33m{catalogo[c]['Gênero'].capitalize()}\033[m")
    print('-=' * 20)


def filtrarLivros(catalogo):
    cont = 0
    print('Para Autor [\033[1;32mAutor\033[m], para Gênero [\033[1;32mGênero\033[m], '
          'Título [\033[1;32mTítulo\033[m] e para para sair [\033[1;32msair\033[m]')
    fil = str(input('\033[1mVocê quer filtar por: Autor, Gênero ou Título?: \033[m')).upper().strip()
    while fil != 'AUTOR' and fil != 'GÊNERO' and fil != 'TÍTULO':
        print('\033[1;31mDigite corretamente!\033[m')
        fil = str(input('\033[1mVocê quer filtar por: Autor, Gênero ou Título?: \033[m')).upper()
    if fil == 'AUTOR':
        a = str(input('\033[1mDigite o nome do autor: \033[m')).upper().strip()
        print('-=' * 20)
        print(f'\033[1;34mFILTRANDO POR {fil.upper()}: {a.upper()}\033[m')
        for c in range(0, len(catalogo)):
            if a == catalogo[c]['Autor'].upper():
                listarFiltro(c, catalogo)
                cont += 1
            else:
                continue

    elif fil == 'GÊNERO':
        b = str(input('\033[1mDigite o gênero: \033[m')).upper().strip()
        print('-=' * 20)
        print(f'\033[1;34mFILTRANDO POR {fil.upper()}: {b.upper()}\033[m')
        for c in range(0, len(catalogo)):
            if b == catalogo[c]['Gênero'].upper():
                listarFiltro(c, catalogo)
                cont += 1
            else:
                continue
    else:
        d = str(input('\033[1mDigite o título do livro: \033[m')).upper().strip()
        print('-=' * 20)
        print(f'\033[1;34mFILTRANDO POR {fil.upper()}: {d.upper()}\033[m')
        for c in range(0, len(catalogo)):
            if d == catalogo[c]['Título'].upper():
                listarFiltro(c, catalogo)
                cont += 1
            else:
                continue

    if cont == 0:
        print('\033[1;34mNão possui livros com esse filtro\033[m')
    else:
        print(f'\033[1;34m{cont} livros encontrados\033[m')


menu()



    
