soma = 0
multa = 10
veiculos = int(input("Digite a quantidade de veículos: "))
while (veiculos != 555):
    if (veiculos > 2):
        pagamento = multa * (veiculos - 2)
        soma = pagamento + soma
    else:
        pagamento = 0
    
    veiculos = int(input("Digite a quantidade de veículos: "))
print (f"Total arrecadado {soma} ")


