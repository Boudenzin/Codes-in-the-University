#Regras de Negócio
impostomil = 0.17
impostomenos = 0.08

#Entrada de Dados
salario = float(input("Qual o valor do seu salário: "))

#Processamento de Dados e Saída de Dados

if (salario >=1000):
    imposto = salario * impostomil
    print (f"O imposto a ser pago é {imposto:.2f}")
else:
    imposto = salario * impostomenos
    print (f"O imposto a ser pago é {imposto:.2f}")
#Final Alternativo
print ("O imposto a ser pago é R$ %.2f" % imposto)
