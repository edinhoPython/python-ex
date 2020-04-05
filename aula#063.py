print('=' * 30)
print(f'{"sequencia de fibonacci":^30}')
print('=' * 30)

termos = int(input('quantos termos quer mostrar ? '))

A = 0
B = 1
C = A + B

print(f'{A} -> ', end="")
print(f'{B} -> ', end="")
for c in range(1,termos - 1):
    print(f'{C} -> ', end="")
    A = B
    B = C
    C = A + B
print(' FIM')