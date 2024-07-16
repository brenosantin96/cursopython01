# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a,b) => 2,1

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Campos'
}

dados_pessoa = {
    'idade': 16,
    'altura' : 1.6
}

pessoa_completa = {**pessoa,**dados_pessoa}

print(pessoa, dados_pessoa)

print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)
    
    
mostro_argumentos_nomeados(nome='Joana', qlqr='123')