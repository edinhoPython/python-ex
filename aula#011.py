largura = float(input('qual a dimensao de sua parede '))
altura = float(input('qual a dimensao de sua parede '))

area = largura * altura
litros = area / 2
print(f'sua parede tem a dimensao de {largura:.2f} X {altura:.2f} = {area}m²')
print(f'para pintar a parede vai precisar de {litros}L de tinta')
