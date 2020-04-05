def contador(i, f, r):
    if r == 0:
        r = 1

    print('~' * 27)
    print(f'contando de {i} ate {f} em {r}')

    if i > f:
        if r > 0:
            r = -r
        else:
            r = +r

    for c in range(i, f, r):
        print(f' {c}', end='')
    print()


contador(1, 10, 1)
contador(10, 0, 2)

contador(i=int(input('inicio ')), f=int(input('final ')), r=int(input('razao ')))