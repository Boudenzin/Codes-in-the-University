#Regras de Negócio

precoconsultaconvenio = 170
precoconsultaparticular = 310

#Entrada de Dados

consultaconvenio = float(input("Olá! Quantas consultas realizadas por convênio você realizou? "))
consultaparticular = float(input("Quantas consultas particulares você realizou? "))

#Processamento de Dados

precototal = (consultaconvenio * precoconsultaconvenio) + (consultaparticular * precoconsultaparticular)

#Saida de Dados

print (f"O valor a receber será R$ {precototal:.2f}")
