palavras = ('curso','elefante','bola','cubo','mais','menos','abisais','python','cachorro')

for letra in palavras:
  palavras_f = letra
  vogais = []
  for letra_f in palavras_f:
    if letra_f == 'a' or letra_f == 'e' or letra_f == 'i' or letra_f == 'o' or letra_f ==  'u':
      vogais.append(letra_f)
    
  print(f'na palavra {palavras_f} temos as vogais {vogais}',end=' ')