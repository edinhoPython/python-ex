pessoas = list()
pessoas_mais_pessadas = list()
pessoas_monos_pessadas = list()
contador_de_pessoas = 0
maior_pesso = 0
menor_pesso = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Pesso: '))

    pessoas.append(nome)
    pessoas.append(peso)

    if contador_de_pessoas == 0:
        maior_pesso = peso
        menor_pesso = peso

    if contador_de_pessoas != 0 and peso > maior_pesso:
        maior_pesso = peso

    if contador_de_pessoas != 0 and peso > menor_pesso:
        menor_pesso = peso

    contador_de_pessoas += 1
    sair = str(input('quer continuar [S/N] ').upper())[0]
    if sair == 'N':
        break

print(f'no total foram {contador_de_pessoas} pessoas cadrastadas')
print(f'o maior pesso foi de {maior_pesso} e foram {pessoas_mais_pessadas}')
print(f'o menor pesso foi de {menor_pesso} e foram {pessoas_monos_pessadas}')
