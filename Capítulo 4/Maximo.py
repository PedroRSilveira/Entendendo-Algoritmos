def maximo(arr):
    if len(arr) == 2:
        if arr[0] >= arr[1]:
            return arr[0]
        else:
            return arr[1]
    sub_max = maximo(arr[1:])
    if arr[0] >= sub_max:
        return arr[0]
    else:
        return sub_max

meuArray = [2, 10, 6, 4]
print(maximo(meuArray))