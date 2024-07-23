import sys

iterable = ['Eu' , 'tenho' , '__iter__']
iterator = iterable.__iter__()

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))