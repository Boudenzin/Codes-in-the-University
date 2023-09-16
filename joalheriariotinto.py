precobolsacouro = 180.00
precobolsatecido = 100.00
precorelogiometal = 215.00
precorelogiocouro = 150.00

presente = input("Que presente você irá comprar? (Relógio/Bolsa) ")
material = input(f"Qual o material do {presente} ")

if (presente == "Relógio"):
    print ("Você ganhou um chaveiro de brinde")
    if (material == "Couro"):
        print (f"O preço do {presente} de {material} ficará por {precorelogiocouro}")
    elif (material == "Metal"):
        print (f"O preço do {presente} de {material} ficará por {precorelogiometal}")
    else:
        print ("Esse material não está disponível")
else:
    if (material == "Tecido"):
        print (f"O preço do {presente} de {material} ficará por {precobolsatecido}")
    else:
        print (f"O preço do {presente} de {material} ficará por {precobolsacouro}")
        

