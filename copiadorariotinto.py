#Regras de Negócio

precopagina = 0.3

#Entrada de Dados

folhas = int(input("Quantas folhas você irá querer imprimir: "))

#Processamento de Dados

pagamento = (folhas * precopagina)

#Saida de Dados

print (f"O valor cobrado pelas {folhas} folhas, vale R$ {pagamento:.2f}")
