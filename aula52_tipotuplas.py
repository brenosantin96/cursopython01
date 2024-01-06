""""
Tipo Tupla - Uma lista Imutavel
"""

nomes = ['Maria', 'Joana', 'Fernanda', 'Tamara']
nomes[1] = 'Outro'

_, _, nome, * resto = nomes
print(nomes)
print(nome)