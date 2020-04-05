valor = float(input('valor do produto '))

desconto = (5 * valor) / 100
total = valor - desconto

print(f'o produto que custava R${valor}, com desconto de 5% vai custar {total:.2f}')