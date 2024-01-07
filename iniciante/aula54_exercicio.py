"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')





"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_compras = []
lista_compras_finalizada = False


while not lista_compras_finalizada:

    opcao_digitada = input(
        f'Selecione uma opção: \n [i]nserir [a]pagar [l]istar \n')

    if opcao_digitada.lower() == 'i':
        item = input("Digite o item que quer adicionar: ")
        lista_compras.append(item)
        continue

    elif opcao_digitada.lower() == 'a':
        indice_digitado = input("Digite o indice do item que quer apagar: ")

        if indice_digitado.isdigit():

            indice = int(indice_digitado)

            try:
                indice_na_lista = lista_compras.index(indice)

                if indice_na_lista != -1:
                    print('Nao existe o item')

                if indice_na_lista:
                    lista_compras.pop(item)
                else:
                    print('Item nao esta disponivel na lista')
            except ValueError:
                print(f'erro')
        else:
            print("Voce digitou alguma coisa que não é o indice da listagem de compras.")

    elif opcao_digitada.lower() == 'l':

        for item in enumerate(lista_compras):
            indice, nome = item
            print(indice, nome)

        continue

    else:
        print('Digite uma opcão válida! \n')
        continue




