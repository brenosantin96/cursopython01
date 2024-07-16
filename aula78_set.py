# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')


s1 = set("Breno")
s2 = {"Breno", "Santin"}
print(s1, type(s1))
print(s2, type(s2))


lista = [1, 2, 3, 3, 3, 3, 1]

s1 = set(lista)
print(s1)

numeros = {1, 2, 3, 3, 3, 3, 1}
print(numeros)


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


setNomes = {"Breno", "Itala", "Bruno"}
setNomes.add("Joao")
setNomes.add("Inacio")
setNomes.add("Ingrid")

setNomes.discard


# Usando um loop for para remover nomes que começam com 'I'
nomes_para_remover = {nome for nome in setNomes if nome.startswith("I")}

for nome in nomes_para_remover:
    setNomes.remove(nome)


print(setNomes)
print(type(setNomes))



setNumeros01 = {1,2,3}
setNUmeros02 = {2,3,4}

setNumeros03Pipe = setNumeros01 | setNUmeros02
setNumeros03And = setNumeros01 & setNUmeros02
setNumeros03Minus = setNumeros01 - setNUmeros02

print("setNumeros03Pipe", setNumeros03Pipe)
print("setNumeros03And", setNumeros03And)
print("setNumeros03Minus", setNumeros03Minus)