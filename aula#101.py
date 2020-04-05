def voto(A):
  ida = 2018 - A
  vota = ''
  if ida < 16:
    vota = ' nao vota'
  elif ida >= 16 and ida < 65:
    vota = ' voto brigatorio'
  elif ida > 65:
    vota = ' voto opcional'
  
  return 'voce tem ' + str(ida) + vota


ano = int(input('ano de nacimento '))
print(voto(ano))