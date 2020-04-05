def area(L,H):
    A = L * H
    print(f'a area do terreno com dimensoes de {L:.2f} X {H:.2f} e de {A:.2f}m²')

area(L = float(input('qual a largura do terreno (m) ')), H = float(input('qual a autura do seu terreno (m) ')))