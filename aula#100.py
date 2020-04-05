from random import randint

def sorteia():
    print('~' * 40)
    num = list()
    print('os numeros sorteado foram:',end='')
    for c in range(1,6):
        n = randint(1,10)
        num.append(n)
        print(f' {n} ',end='')
    soma_par(num)

def soma_par(num):
    print()
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'a soma dos numeros {num} e de {soma}')
    print('~' * 40)

sorteia()
sorteia()
sorteia()