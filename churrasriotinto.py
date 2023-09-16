#Regras de Negócio

latasporpessoa = 6
carneporpessoa = 0.4
precoquilo = 41
precocerveja = 5.2

#Entrada de Dados

pessoas = int(input("Quantas pessoas aceitaram o convite do seu churras? "))

#Processamento de Dados

carne = (carneporpessoa * pessoas) * precoquilo
cerveja = (latasporpessoa * pessoas) * precocerveja

#Saída de Dados

print (f"Você gastará R$ {carne:.2f} com carne")
print (f"Você também gastará R$ {cerveja:.2f} com cerveja, boa sorte")

