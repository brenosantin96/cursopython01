# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multArgs(*args):
    resultado = 1
    for i in args:
        resultado = resultado * i

    return resultado


valores = multArgs(2, 2, 2, 2, 2)
print(valores)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def isEven(num: int) -> bool:
    return num % 2 == 0


print(isEven(2))
print(isEven(3))
print(isEven(4))
print(isEven(5))

