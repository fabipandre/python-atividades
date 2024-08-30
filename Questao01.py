# Mensagem de boas vindas
print("Bem-vindo ao aplicativo de vendas da empresa Fabiana Pereira Andre 304787!")

# input do valor do produto e da quantidade
valor_unitario = float(input("Entre com o valor unitário do produto: R$ "))
quantidade = int(input("Entre com a quantidade do produto: "))

# calculo do total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# calculo do desconto
if valor_total_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_total_sem_desconto < 6000:
    desconto = 4
elif 6000 <= valor_total_sem_desconto < 10000:
    desconto = 7
else:
    desconto = 11

#  Cálculo do valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * (desconto / 100))

# Apresentação de saída no console
print("Pedido recebido!")
print(f"O valor sem desconto foi R${valor_total_sem_desconto:.2f}")
print(f"O valor com desconto foi R${valor_total_com_desconto:.2f} (desconto {desconto}%)")
