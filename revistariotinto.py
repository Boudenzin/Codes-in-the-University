#Entrada de Dados

revistas = int(input("Qual a quantidade total de revistas que você possui? "))
amigos = int(input("Para quantos amigos você irá querer doar as suas revistas? "))

#Processamento de Dados

revistasporamigos = revistas // amigos
revistasrestantes = revistas % amigos

#Saida de Dados
print (f"Você doará {revistasporamigos} revistas para cada pessoa e sobrarão {revistasrestantes} revistas")
