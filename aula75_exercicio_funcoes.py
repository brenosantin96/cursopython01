# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def duplicador(number):
    return number * 2
    
def triplicador(number):
    return number * 3

def quadriplicador(number):
    return number * 4


print(duplicador(2))
print(triplicador(2))
print(quadriplicador(2))



def multiplier(number):
    def multiplierInside(numberToMultiply):
        return number * numberToMultiply
    
    return multiplierInside


result = multiplier(5)

print(result(3))


def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply


duplicar = create_multiplier(2)
triplicar = create_multiplier(3)
quadriplicar = create_multiplier(4)

print(duplicador(2))
print(triplicar(2))
print(quadriplicar(2))