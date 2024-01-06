"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultado_01s:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado_01 anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado_01 anterior for maior que 9:
    resultado_01 é 0
contrário disso:
    resultado_01 é o valor da conta

O segundo dígito do CPF é 0
"""

# 74682489070

cpf = input("Digite seu CPF: ")
cpf_09_primeiros_digitos = cpf[:9]

fatores_01 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
fatores_02 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

if cpf.isdigit() and len(cpf_09_primeiros_digitos) == 9:

    resultado_01 = 0
    resultado_02 = 0

    try:
        array_item_cpf = [int(digito)
                          for digito in cpf_09_primeiros_digitos]

        # estou criando um array, estou retornando para o array o digito_cpf (que é retornado pelo enumerate) * o valor de cada indice de fatores_01
        # como na primeira iteracao o indice é 0, vai pegar o valor 10 e multiplicar pelo primeiro digito do CPF, e assim sucessivamente...
        new_array_item_cpf = [digito_cpf * fatores_01[indice]
                              for indice, digito_cpf in enumerate(array_item_cpf)]
        soma_numeros_multiplicacao = (sum(new_array_item_cpf)) * 10
        resto = soma_numeros_multiplicacao % 11

        if resto > 9:
            resultado_01 = 0
            print(f'Primeiro digito do CPF é {resultado_01}')
            array_item_cpf.append(resultado_01)

            new_array_item_cpf_2 = [digito_cpf * fatores_02[indice] for indice,
                                    digito_cpf in enumerate(array_item_cpf)]

            soma_numeros_multiplicacao_02 = (sum(new_array_item_cpf_2)) * 10
            resto_02 = soma_numeros_multiplicacao_02 % 11
            
            resultado_02 = resto_02 if resto_02 <= 9 else 0 #ternario
            print(f'Segundo digito do CPF é {resultado_02}')
            

        else:
            resultado_01 = resto
            print(f'Primeiro digito do CPF é {resultado_01}')
            array_item_cpf.append(resultado_01)

            new_array_item_cpf_2 = [digito_cpf * fatores_02[indice] for indice,
                                    digito_cpf in enumerate(array_item_cpf)]
            
            soma_numeros_multiplicacao_02 = (sum(new_array_item_cpf_2)) * 10
            resto_02 = soma_numeros_multiplicacao_02 % 11
            
            resultado_02 = resto_02 if resto_02 <= 9 else 0 #ternario
            print(f'Segundo digito do CPF é {resultado_02}')

            

    except Exception as err:
        print(f'Algum erro aconteceu: {err}')


else:
    print("Digite apenas numeros para o CPF. Digite apenas 09 digitos")
