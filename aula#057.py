sexo = str(input('qual o seu sexo [M/F] ').upper())
sexo1 = sexo

if sexo1 not in ('MF'):
  sexo2 = sexo
  while sexo2 not in ('MF'):
    sexo = str(input('sexo invalido tente novamente ').upper())
    sexo2 = sexo
  
  print(f'sexo {sexo2} valido')
else:
  print(f'sexo {sexo} valido')
