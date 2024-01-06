"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])


variavel = 'breno santin'

name = variavel.split(' ')

print(name[0])
print(name[1])
print(f'tamanho do name[0] é {len(name[0])}')

