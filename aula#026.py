frase = str(input('digite uma frase: ').upper()).strip()
cont_a = 0
for l in frase:
    if l == 'A':
        cont_a += 1

print(f'a letra A apareceu {cont_a} vezes')
print(f'a primeira letra A apareceu na posicao {frase.find("A") + 1}')
print(f'a utima letra A apareceu na casa {frase.rfind("A") + 1}')