#Funcoes de primeria classe
#High order functions

def greeting(msg, nome):
    return f'{msg}, {nome}!'

def exec(func, *args):
    return func(*args)

greeting_2 = greeting

print(
    exec(greeting_2, "Bom dia", "Breno")
)

"""
High Order Functions (Funções de Ordem Superior) em Python são funções que atendem a pelo menos um dos seguintes critérios:

Podem receber uma ou mais funções como argumentos.
Podem retornar uma função como resultado.


"""

