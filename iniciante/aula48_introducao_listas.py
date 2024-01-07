"""
Listas em Python
Tipo LIST = Mutavel

Metodos uteis: append, insert, pop, del, clear, extend

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""

string = 'ABCDE' #5 caracteres
lista = [123, True, 'Breno Santin', 1.2, []]


print(lista)
print(type(lista))
print(lista[2].upper())

listanumeros = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
listanumeros.append(50)
listanumeros.pop()
listanumeros.append(60)
listanumeros.append(70)
del listanumeros[-1]
# lista.clear()
listanumeros.insert(100, 5)
print(listanumeros[4])
ultimo_valor = listanumeros.pop(3)
print(listanumeros, 'Removido,', ultimo_valor)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

#IMPORTANTE:

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

lista_exercicio = ['Maria', 'Helena', 'Luiz']

for nome in lista_exercicio:
    print(f'{lista_exercicio.index(nome)} - {nome}')
    
    
    """
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""


listaexercicio2 = ['Maria', 'Helena', 'Luiz']
listaexercicio2.append('João')


indices = range(len(listaexercicio2))

for indice in indices:
    print(indice, listaexercicio2[indice], type(listaexercicio2[indice]))