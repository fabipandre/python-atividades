# define da função de escolha do serviço
def escolha_servico():
    while True:
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitação')
        print('ICO - Impressão Colorida')
        print('IBO - Impressão Preto e Branco')
        print('FOT - Fotocópia')

        tipo_servico = input('>>').lower()

        if tipo_servico != 'dig' and tipo_servico != 'ico' and tipo_servico != 'ibo' and tipo_servico != 'fot':
            print('Escolha inválida. Entre com o tipo de serviço desejado novamente.')
            continue

        if tipo_servico == 'dig':
            return 1.10
        elif tipo_servico == 'ico':
            return 1
        elif tipo_servico == 'ibo':
            return 0.40
        elif tipo_servico == 'fot':
            return 0.20

    return tipo_servico


# define a função do cálculo de desconto de acordo com o número de páginas
def num_pagina():
    while True:
        try:
            num_paginas = int(input('\nEntre com o número de páginas: '))

            if num_paginas < 20:
                return num_paginas
            elif 20 <= num_paginas < 200:
                return num_paginas - (num_paginas * 0.15)
            elif 200 <= num_paginas < 2000:
                return num_paginas - (num_paginas * 0.20)
            elif 2000 <= num_paginas < 20000:
                return num_paginas - (num_paginas * 0.25)
            else:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                print('')
                continue

        except ValueError:
            print('Oops!! Número inválido. Tente novamente...')


# define a função de opções de serviço extra
def servico_extra():
    while True:
        print('Deseja adicionar mais algum serviço?')
        print('1 - Encadernação Simples - R$ 10,00')
        print('2 - Encadernação Capa Dura - R$ 25,00')
        print('0 - Não desejo mais nada')

        try:
            opcao_extra = int(input('>>'))

            if opcao_extra != 1 and opcao_extra != 2 and opcao_extra != 0:
                continue

            if opcao_extra == 1:
                return 10
            elif opcao_extra == 2:
                return 25
            else:
                return 0

        except ValueError:
            print('Oops!! Número inválido. Tente novamente...')


# Mensagem de boas-vindas
print('Bem-vindo a Gráfica e copiadora Fabiana Pereira Andre!\n')

# chama a função de escolha do serviço
servico = escolha_servico()

# chama a função de número de páginas que define o desconto
num_pagina = num_pagina()

# chama função para seleção de serviço extra
extra = servico_extra()

# cálculo do valor total
total = servico * num_pagina + extra

print('Total (R$) {} (serviço : {} * páginas: {} + extra(s): {})'.format(total, servico, num_pagina, extra))
