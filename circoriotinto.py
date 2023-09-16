#Regras de Negócio
precocriancas = 5.00
precoidosos = 15.00
precodemais = 25.00

#Entrada de Dados
idade = int(input("Bem vindo ao Circo Desmantelo! Qual a sua idade, não permitimos menores de 0 anos: "))

#Processamento de Dados
if (idade>=60):
    print (f"Pague R$ {precocriancas} ao banco")
elif (idade<=5):
    print (f"pague R$ {precoidosos} ao banco")
else:
    print (f"Pague R$ {precodemais} ao banco")
