"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

      012 345 678 90
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

""" 
numero = 12359489124
numero_string = str(numero)
#criando uma variavel chamada digito, vai popular o array com cada item da variavel
array_numeros = [int(digito) for digito in numero_string]
print(array_numeros)
#[1, 2, 3, 5, 9, 4, 8, 9, 1, 2, 4]   
# """


import os
cpf = input("Digite os 09 primeiro digitos do seu CPF: ")

fatores = [10, 9, 8, 7, 6, 5, 4, 3, 2]

if cpf.isdigit() and len(cpf) == 9:

    resultado = 0

    try:
        array_item_cpf = [int(digito)
                          for digito in cpf]

        # estou criando um array, estou retornando para o array o digito_cpf (que é retornado pelo enumerate) * o valor de cada indice de fatores
        # como na primeira iteracao o indice é 0, vai pegar o valor 10 e multiplicar pelo primeiro digito do CPF, e assim sucessivamente...
        new_array_item_cpf = [digito_cpf * fatores[indice]
                              for indice, digito_cpf in enumerate(array_item_cpf)]
        soma_numeros_multiplicacao = (sum(new_array_item_cpf)) * 10
        resto = soma_numeros_multiplicacao % 11

        if resto > 9:
            resultado = 0
            print(f'Primeiro digito do CPF é {resultado}')
        else:
            resultado = resto
            print(f'Primeiro digito do CPF é {resultado}')

    except Exception as err:
        print(f'Algum erro aconteceu: {err}')


else:
    print("Digite apenas numeros para o CPF. Digite apenas 09 digitos")
