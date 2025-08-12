def recursiva(i):
    print(i)
    if i <= 1:
        return
    else:
        recursiva(i-1)

recursiva(5)