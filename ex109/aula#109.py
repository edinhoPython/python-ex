import moeda

p = float(input('um valor R$: '))

print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'{moeda.moeda(p)} com aumento de 10% é {moeda.aumento(p, 10, True)}')
print(f'{moeda.moeda(p)} com desconto de 10% é {moeda.desconto(p, 10, True)}')