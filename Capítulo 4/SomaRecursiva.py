def soma(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + soma(arr[1:])
  
meuArray = [2, 4, 6]
print(soma(meuArray))