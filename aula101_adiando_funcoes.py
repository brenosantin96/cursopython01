def soma(x,y):
    return x + y


def multiplica(x,y):
    return x * y

def criar_funcao_operadora(typeFunction, args):
    def newFunction(x):
        if typeFunction == '*':
            return x * args
        if typeFunction == '+':
            return x + args
        if typeFunction == '-':
            return x - args
        if typeFunction == '/':
            return x / args
    return newFunction



soma_com_cinco = criar_funcao_operadora("+",5)
multiplica_por_dez = criar_funcao_operadora("*",10)

print(soma_com_cinco(3))
print(multiplica_por_dez(2))


print()
print()
print("SOLUCAO PROFESSOR")
print()
print()
# Exercício - Adiando execução de funções
def soma2(x, y):
    return x + y


def multiplica2(x, y):
    return x * y


def criar_funcao2(funcao, x):
    def interna2(y):
        return funcao(x, y)
    return interna2


soma_com_cinco2 = criar_funcao2(soma, 5)
multiplica_por_dez2 = criar_funcao2(multiplica, 10)

print(soma_com_cinco2(10))
print(multiplica_por_dez2(10))