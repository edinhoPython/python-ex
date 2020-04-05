distancia = int(input('qual a distancia da sua viagem ? '))

if distancia <= 200:
    valor = distancia * 0.50

elif distancia > 200:
    valor = distancia * 0.45

print(f'o valor da passagem e de {valor:.2f}')