# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy


dicti01 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0,1,2]
}

#Aqui estamos apontando na memora do dicti01
#Tem que usar o DEEP COPY para nao alterar o original
#SHALLOW COPY nao COPIA variaveis mutaveis (lists, dicts, objetos)
dicti02 = copy.deepcopy(dicti01)

dicti02['c1'] = 1000
dicti02['l1'][1] = 9999

print("Dicti01: ", dicti01)
print("Dicti02: ", dicti02)


pessoa = {
    'nome' : 'Breno',
    'sobrenome' : 'Santin',
    'idade': 22
}

# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro