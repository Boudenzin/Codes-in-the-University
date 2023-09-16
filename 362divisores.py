qtddivisores = 0




numerodividendo = int(input("Digite o número que você quer saber os seus divisores: "))
for testedivisor in range (1, (numerodividendo + 1)):
    if ((numerodividendo) % testedivisor == 0):
        qtddivisores += 1
print (f"O número {numerodividendo} tem {qtddivisores} divisores")
