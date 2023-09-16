preco2d = 8.50
preco3d = 14.50
combosimples = 10.00
combocompleto = 12.00

filme = input("O filme será 3D ou 2D? ")
resposta = input("Temos o COMBO SIMPLES, com refri e pipoca, e temos o COMBO COMPLETO que tem refri, pipoca e chocolate. Vai querer um deles? (S/N) : ")

if (filme == "2D"):
    valortotal = preco2d

else:
    valortotal = preco3d

if (resposta == "S"):
    lanche = input("Combo Simples ou Combo Completo? ")
    
    if (lanche == "Combo Simples"):
        valortotal = valortotal + combosimples
        
    else:
        valortotal = valortotal + combocompleto

print (f"O valor total do seu pedido é R$ {valortotal}")


    
