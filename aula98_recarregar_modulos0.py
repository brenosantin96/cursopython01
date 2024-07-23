import importlib

import aula98_recarregar_modulos1

print(aula98_recarregar_modulos1.variavel)

for i in range(10):
    importlib.reload(aula98_recarregar_modulos1)
    print(i)

print('Fim')