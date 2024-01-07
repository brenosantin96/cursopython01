input_name = input("Digite seu nome: ")
input_idade = input("Digite sua idade: ")

reverse_name = input_name[::-1]
qnt_spaces = input_name.count(" ")
space_key = len(input_name)

if input_name and input_idade:
    print(f'Seu nome é {input_name}')
    print(f'Seu nome invertido é {reverse_name}')
    
    if " " in input_name:
        print("Seu nome contém espacos")
    else:
        print("Seu nome nao contem espacos")
    
    print(f'Seu nome contém {qnt_spaces} espacos')
    print(f'Seu nome possui {len(input_name)} letras')
    print(f'A primeira letra do seu nome é {input_name[0]}')
    print(f'A ultima letra do seu nome é {input_name[-1]}')
else:
    print("Desculpe, voce deixou campos vazios")
