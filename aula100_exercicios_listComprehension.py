# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

produtos2 = copy.deepcopy(produtos)

produtos2 = [
    {**produto, "preco" : round(produto['preco'] * 1.10, 2)}
    for produto in produtos2
]

produtos_ordenados_por_nome_decrescente = sorted(produtos2, key=lambda x: x['nome'], reverse=True)
produtos_ordenados_preco = sorted(produtos2, key=lambda x: x['preco'], reverse=True)

print("produtos_ordenados_por_nome_decrescente")
print(*produtos_ordenados_por_nome_decrescente, sep="\n")

print()
print()

print("produtos_ordenados_preco")
print(*produtos_ordenados_preco, sep="\n")


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
