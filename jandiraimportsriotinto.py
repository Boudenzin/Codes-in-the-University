precocelularmotorola = 879.18
precocelularsamsung = 921.40
precotabletmultilaser = 339.50
precotabletsamsung = 417.22

aparelho = str.upper(input("Qual o tipo de aparelho que você quer? "))
modelo =  str.upper(input("Qual o modelo que você irá querer? "))
quantidade = int(input("Qual a quantidade desejada? "))

if (aparelho == "CELULAR"):
    if (modelo == "SAMSUNG"):
        precototal = precocelularsamsung
    else:
        precototal = precocelularmotorola
else:
    if (modelo == "MULTILASER"):
        precototal = precotabletmultilaser
    else:
        precototal = precotabletsamsung

precototal = precototal * quantidade

print (f"O valor a ser pago é R${precototal:.2f}")
        
    

