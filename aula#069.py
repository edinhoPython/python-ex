pessoas18 = 0
homen = 0
mulheres = 0

while True:
  print('='*10)
  print('cadastre uma pessoas')
  print('='*10)

  idade = int(input('idade: '))
  sexo = str(input('sexo [M/F] ')).upper() [0]

  if idade >= 18:
    pessoas18 += 1
  
  if sexo == 'M':
    homen += 1
  
  if sexo == 'F' and idade <= 20:
    mulheres += 1

  conti = str(input('quer continuar ')).upper() [0]
  if conti == 'N':
    break

print(f'pessoas com mais de 18 anos: {pessoas18}')
print(f'au todo temos {homen} cadastrado')
print(f'foram {mulheres} mulheres com menos de 20 anos')
