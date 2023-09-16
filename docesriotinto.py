#Regras de Negócio
precobeijinhos = 1.7
precobrigadeiros = 1.9

#Entrada de Dados
brigadeiros = int(input("Olá! Quantos brigadeiros você irá querer? "))
beijinhos = int(input("Quantos beijinhos você irá querer? "))
criancas = int(input("Quantas crianças irão para a sua festa? "))

#Processamento de Dados
precototal = (beijinhos * precobeijinhos) + (brigadeiros * precobrigadeiros)
docepcrianca = (beijinhos + brigadeiros)//criancas

#Saída de Dados
print (f"O total gasto será de R$ {precototal:.2f} e teremos {docepcrianca} docinhos para cada criança")
