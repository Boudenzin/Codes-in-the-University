taxaexaluno = 60.00
convidados12mais = 50
convidados3a11anos = 25
convidadosmenos3 = 0

participante = str.upper(input("Qual o tipo do participante? "))

if (participante == "EX-ALUNO"):
    totalpago = taxaexaluno
else:
    idade = int(input("Qual a idade do convidado? "))
    if (idade >= 12):
        totalpago = convidados12mais
    elif (idade > 3):
        totalpago = convidados3a11anos
    else:
        totalpago = convidadosmenos3

print (f"O valor total a ser pago é de R$ {totalpago:.2f}")
        
