def maior(*num):
    print('-=' * 20)
    print('os valores foram',end='')
    cont = 0
    for c in num:
        print(f' {c}',end='')
        cont += 1
    print(f' foram {cont} valores')
    print(f'o maior valor foi {max(num)}')

maior(1,2,4,3,5,6)
maior(2,3,4,1)
maior(3,9,8,9,9,1)
maior(1,1,2,4,7,8,5)