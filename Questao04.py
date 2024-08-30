# import do módulo sys
import sys

# definição de variáveis
lista_livro = []
id_global = 0


# define a função que monta o menu de opções
def menu():
    # global id_global

    print('\n----------------- MENU PRINCIPAL -----------------')
    print('1) Cadastrar Livro ')
    print('2) Consultar Livro')
    print('3) Remover Livro')
    print('4) Encerrar Programa')

    # Fica em loop até que a opção 4 seja digitada. Então, termina o programa
    while True:
        try:
            opcao = int(input('Informe a opção: '))

            if opcao <= 0 or opcao > 4:
                print('Opção inválida!!!')
                continue

            if opcao == 1:
                cadastrar_livro(id_global)
                break
            elif opcao == 2:
                consultar_livro()
                break
            elif opcao == 3:
                remover_livro()
                break
            elif opcao == 4:
                print('Encerrando programa...')
                sys.exit(0)

        except ValueError:
            print("Opção inválida. Informe um número entre 1 e 4.")


# define a função de cadastro de livro
def cadastrar_livro(id):
    global id_global

    print('***************************************************')
    print('\n----------------- MENU CADASTRAR LIVRO -----------------')

    livro = {
        'id': id,
        'nome': input('Entre com o nome do livro: '),
        'autor': input('Entre com o nome do autor: '),
        'editora': input('Entre com o nome da editora : ')
    }

    # adiciona o dicionário de livro à lista
    lista_livro.append(livro.copy())

    print('\nLivro cadastrado com sucesso!\n')

    # incrementa o contador do ID global
    id_global = id_global + 1

    # mostra menu principal
    menu()


# lista todos os livros
def listar_livros():
    if len(lista_livro) == 0:
        print('Não há livros cadastrados!\n')

    for livro in lista_livro:
        imprime_livro(livro)

    menu_consulta()


# define função de consulta por id
def consultar_livro_por_id():
    if len(lista_livro) == 0:
        print('Não há livros cadastrados!\n')

    try:
        id_livro = int(input('Entre com o id do livro: '))
        livro_encontrado = pesquisa_elemente_por_id(id_livro, lista_livro)
        imprime_livro(livro_encontrado)

    except ValueError:
        print('Valor inválido')

    menu_consulta()


# define função de consulta por autor
def consultar_livro_por_autor():
    autor = None

    if len(lista_livro) == 0:
        print('Não há livros cadastrados!\n')
        # menu()

    encontrou = False
    lista_livros_autor = []

    try:
        autor = input('Entre com o nome do autor: ')
        for livro in lista_livro:
            if livro['autor'].lower() == autor.lower():
                lista_livros_autor.append(livro)
                encontrou = True

    except ValueError:
        print('Valor inválido')

    if encontrou:
        for livro in lista_livros_autor:
            imprime_livro(livro)
    else:
        print("Livro nao encontrado para o autor {}".format(autor))

    menu_consulta()


# define o menu de consulta de livros
def menu_consulta():
    print('\nSelecione a opção')
    print('1. Consultar Todos')
    print('2. Consultar por Id')
    print('3. Consultar por Autor')
    print('4. Retornar ao menu')


# define função de sub-menu de consulta de livros
def consultar_livro():
    print('***************************************************')
    print('\n----------------- MENU CONSULTAR LIVRO -----------------')

    menu_consulta()

    while True:
        try:
            opcao = int(input('>> '))

            if 0 >= opcao > 4:
                raise ValueError()

            if opcao == 1:
                listar_livros()
            elif opcao == 2:
                consultar_livro_por_id()
            elif opcao == 3:
                consultar_livro_por_autor()
            elif opcao == 4:
                menu()

        except ValueError:
            print('Opção inválida')


# Function para encontrar um elemento pelo ID
def pesquisa_elemente_por_id(id, list):
    for element in list:
        if element['id'] == id:
            return element
    return None  # Retorna None se o elemento não for encontrado


# define a função de remoção de livro da lista através do id
def remover_livro():
    print('\n----------------- MENU REMOVER LIVRO -----------------')
    print('***************************************************')

    if len(lista_livro) == 0:
        print('Não há livros cadastrados!\n')
        menu()

    print('Entre com o id do colaborador a ser removido')

    try:
        id_livro = int(input('>> '))

        livro_encontrado = pesquisa_elemente_por_id(id_livro, lista_livro)

        if livro_encontrado:
            lista_livro.remove(livro_encontrado)
            print('Livro removido com sucesso!')
            menu()

    except ValueError:
        print('Parâmetro inválido')
    except IndexError:
        print('id inválido. Tente novamente')


# Imprime as informações do livro na console
def imprime_livro(livro):
    print('------------------------------------------------')
    print('id : {}'.format(livro['id']))
    print('nome : {}'.format(livro['nome']))
    print('autor : {}'.format(livro['autor']))
    print('editora : {}'.format(livro['editora']))


# Mensagem de boas vindas
print("Bem-vindo ao aplicativo de Fabiana Pereira Andre\n")

# chama a função para mostrar o menu principal
menu()
