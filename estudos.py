""" 
numero = 12359489124
numero_string = str(numero)
#criando uma variavel chamada digito, vai popular o array com cada item da variavel
array_numeros = [int(digito) for digito in numero_string]
print(array_numeros)
#[1, 2, 3, 5, 9, 4, 8, 9, 1, 2, 4]   
# """



lista = ['Maria', 'joao', 'Fernando']
lista.append("Joao")
lista.append("Julio")
lista.append("Jeferson")
lista.append("Janaina")
lista.append("Jane")

exemplo_enumerate = enumerate(lista)
print(exemplo_enumerate) #<enumerate object at 0x000001C7C9B5DC10>

for item in exemplo_enumerate:
    a, b = item
    print(a, b)

#a de cima e de baixo sao a mesma coisa!


for indice, nome in enumerate(lista):
    print(indice, nome)



""" 

import os
cpf = input("Digite seu CPF: ")

if cpf.isdigit():
    
    try:
        array_item_cpf = [int(digito)for digito in cpf]
        new_array_item_cpf = array_item_cpf
        print(array_item_cpf)
        
    except Exception as err:
        print(f'Algum erro aconteceu: {err}')
    
       
    
else:
    print("Digite apenas numeros para o CPF.")
    

    
 """

