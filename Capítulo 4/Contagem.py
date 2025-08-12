def contagem(arr):
    if arr ==[]:
        return 0
    else:
        return 1 + contagem(arr[1:])
        
meuArray = [2, 4, 6]
print(contagem(meuArray))