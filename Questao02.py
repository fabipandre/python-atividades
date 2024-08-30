# Mensagem de boas vindas
print("Seja bem vindo a loja de Gelados Fabiana Pereira Andre")

# Apresenta cardapio para usuario
print("---------------------Cardápio----------------------")
print("------| Tamanho | Cupuaçu (CP) |  Açai (AC) |------")
print("------|    P    |   R$  9,00   |  R$ 11,00  |------")
print("------|    M    |   R$ 14,00   |  R$ 16,00  |------")
print("------|    G    |   R$ 18,00   |  R$ 20,00  |------")
print("---------------------------------------------------")

# declara acumulador com valor inicial
soma = 0

# laco de repetição para tratar as entradas feitas pelo usuário  e cálculo das combinações de pedidos
while True:
    sabor = input("Digite o sabor desejado Cupuaçu (CP) ou Açaí(AC): ")
    sabor = sabor.upper()

    if sabor != "CP" and sabor != "AC":
        print("Sabor Inválido. Tente Novamente!!")
        continue
    print("")

    tamanho = input("Digite o tamanho desejado (P, M ou G):")
    tamanho = tamanho.upper()

    print("")
    if tamanho != "P" and tamanho != "M" and tamanho != "G" :
        print("Tamanho Inválido. Tente Novamente!!")
        continue

    if sabor == "CP":
        if tamanho == "P":
            soma += 9
            print("Você pediu Cupuaçu (CP) tamanho P: R$ 9.00")
        elif tamanho == "M":
            soma += 14
            print("Você pediu Cupuaçu (CP) tamanho M: R$ 14.00")
        elif tamanho == "G":
            soma += 18
            print("Você pediu Cupuaçu (CP) tamanho G: R$ 18.00")

    elif sabor == "AC":
        if tamanho == "P":
            soma += 11
            print("Você pediu Açaí (AC) tamanho P: R$ 11.00")
        elif tamanho == "M":
            soma += 16
            print("Você pediu Açaí (AC) tamanho M: R$ 16.00")
        elif tamanho == "G":
            soma += 20
            print("Você pediu Açaí (AC) tamanho G: R$ 20.00")

    # Apresenta opção para o usuário finalizar o pedido
    pergunta = input("Deseja pedir mais alguma coisa?(S/N)").upper()
    if pergunta == "N":
        break

# Apresenta o valor total do pedido
print(f"Valor Total é de R${soma:.2f}")

