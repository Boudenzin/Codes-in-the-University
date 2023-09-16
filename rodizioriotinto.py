#Regras de Negócio
rodiziogratis = 10

#Entrada de Dados

convidados = int(input("Quantos convidados você convidou para o seu aniversário? "))
precorodizio = float(input("Qual o preço do rodízio? "))

#Processamento de Dados

rodiziogratis = convidados // rodiziogratis
precototal = (convidados - rodiziogratis) * precorodizio

#Saída de Dados

print (f"O valor total a pagar será de R$ {precototal:.2f}")
