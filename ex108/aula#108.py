import moeda

v = float(input('um volor R$ '))

print(f'o dobro de {moeda.moeda(v)} e {moeda.moeda(moeda.dobro(v))}')
print(f'a metade de {moeda.moeda(v)} e {moeda.moeda(moeda.metade(v))}')
print(f'{moeda.moeda(v)} com aumento de 10% e {moeda.moeda(moeda.aumento(v, 10))}')
print(f'{moeda.moeda(v)} com desconto de 10% e {moeda.moeda(moeda.desconto(v, 10))}')