# Hash para evitar duplicatas em uma votação

votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Já votou")
    else:
        votaram[nome] = True
        print("Ainda não votou")

verifica_eleitor("Tom")
verifica_eleitor("Mike")
verifica_eleitor("Mike")