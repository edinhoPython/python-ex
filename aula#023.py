numero = int(input('um numero '))
u = numero // 1 % 1
d = numero // 1 % 10
c = numero // 1 % 100
m = numero // 1 % 1000

print(f'analizando o numero {numero}')
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')