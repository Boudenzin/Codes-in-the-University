tempominimo = 55
beneficio = 0.6
bonus = 0.15

tempo = int(input("Quanto tempo você já contribuiu para o INSS? "))
salario = float(input("Qual o seu salário atual? "))

if (tempo < tempominimo):
    print ("Não tem direito ao benefício")

else:
    totalpago = beneficio * salario
    if (tempo > tempominimo):
        bonustotal = bonus * (tempo - tempominimo)
        totalpago = totalpago + (salario * bonustotal)
    print (f"Você receberá R$ {totalpago:.2f}")
    
