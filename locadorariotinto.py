multaatedois = 30.00
multaatetres = 80.00
multamaiortres = 40.00

diaria = float(input("Seja bem vind@ a nossa locadora, digite o valor da diária: "))
dias = int(input("Quantos dias você alugou o carro? "))
tempoatraso = int(input("Caso houver atraso na devolução, informar o valor em horas: "))

valortotal = diaria*dias

if (tempoatraso == 0):
    print(f"Já que não houve atraso, o valor a ser pago é equivalente a R$ {valortotal:.2f}")

elif (tempoatraso < 2):
    valortotal = valortotal + multaatedois
    print (f"Já que houve atraso, com multa de R$ {multaatedois}, o valor a ser pago é R$ {valortotal:.2f}")

elif (tempoatraso > 3):
    multamaiortres = multamaiortres * tempoatraso
    valortotal = valortotal + multamaiortres
    print (f"Já que houve atraso, com multa de R$ {multamaiortres}, o valor a ser pago é R$ {valortotal:.2f}")

else:
    valortotal = valortotal + multaatetres
    print (f"Já que houve atraso, com multa de R$ {multaatetres}, o valor a ser pago é R$ {valortotal:.2f}")

    
