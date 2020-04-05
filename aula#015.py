dias = int(input('quantos dia o carro foi alugado '))
km = float(input('quantos km andei '))
total = (dias * 60) + (km * 0.15)

print(f'o total a pagar e de R${total:.2f}')