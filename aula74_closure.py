"""
Closure e funções que retornam outras funções
closures são funções internas que lembram o estado do seu ambiente onde foram criadas. 
Em outras palavras, uma closure é uma função aninhada que captura as variáveis locais do escopo em que foi definida, 
mesmo depois que o escopo externo é finalizado. As closures são úteis para criar funções 
com comportamento personalizado e persistente
"""


def create_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    return greet


say_good_morning = create_greeting("Bom dia")
say_good_night = create_greeting("Boa noite")

print(say_good_morning("Joao"))
print(say_good_night("Zequinha"))
