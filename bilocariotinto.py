#Regras de Negócio

pesoprato = 230
precoquilo = 40

#Entrada de Dados

peso = int(input("Qual foi a pesagem da refeição, coloque o valor em gramas, por favor: "))

#Processamento de Dadsos
quilo = (peso-pesoprato)
pagamento = precoquilo* (quilo/1000)

#Saida de Dados

print (f"O preço da refeição foi R$ {pagamento:.2f}")
