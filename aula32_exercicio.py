"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

"""
#Primeiro EXERCICIO
numero_input = input("Digite um numero inteiro: ")

try:
    numeroInt = int(numero_input)
    if(numeroInt % 2 == 0):
        print("Esse numero é par")
    else:
        print("Esse numero nao é par.")
except:
    print('Isso não é um numero inteiro')
"""


"""
#SEGUNDO EXERCICIO
hora_input = input("Digite a hora atual: ")

try:
    hora_int = int(hora_input)
    if (hora_int >= 0 and hora_int <= 11):
        print("Bom dia")
    elif (hora_int >= 12 and hora_int <= 17):
        print("Boa tarde")
    elif (hora_int >= 18 and hora_int <= 23):
        print("Boa noite")
except:
    print("Digite apenas um numero inteiro para identificar a hora")
"""

name_input = input("Digite seu nome: ")
name_count = len(name_input)

if not name_input.isalpha():
    print("Digite apenas letras alfabeticas.")
elif name_count <= 4:
    print("Seu nome é curto")
elif name_count > 4 and name_count <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

