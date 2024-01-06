"""""
Calculadora com while
"""""

while True:

    numero_1 = input("Digite o primeiro numero: ")
    numero_2 = input("Digite o segundo numero: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except Exception as error:
        numeros_validos = None
        print(error)

        if numeros_validos is None:
            print('Um dos numeros digitados são inválidos.')
            continue
    
    operadores_aritmeticos = "+-/*"
    
    if operador not in operadores_aritmeticos:
        print('Operador invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    
    print('Realizando sua conta, confira o resultado abaixo: ')
    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}')
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}')
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}')
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = {(numero_1_float * numero_2_float):.2f}')
    else:
        print('Nunca deveria chegar aqui')

    ####
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair:
        break
