# Dígrafo (grafo direcionado) com dicionário

from collections import deque

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"]  = []
grafo["thom"] = []
grafo["jonny"] = []

# print(grafo)

def pessoa_e_vendedor(nome):
    # Para esse exemplo é vendedor de manga se o nome termina em 'm'
    return nome[-1] == 'm'

# BFS (Esse é um algoritmo de busca em largura)
def busca(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

busca("voce")