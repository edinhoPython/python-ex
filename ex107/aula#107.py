import moedas

p = int(input('um valor R$ '))

print(f'A metade de {p} e {moedas.metade(p)}.')
print(f'O dobro de {p} e {moedas.dobro(p)}')
print(f'{p} aumento de 10% e {moedas.aumento(p, 10)}')
print(f'{p} com um desconto de 10% {moedas.desconto(p, 10)}')
