ano = int(input('em que ano o atleta naceu '))

ano_final = 2018 - ano

if ano_final <= 9:
  print(f'quem naceu em {ano} tem {ano_final} anos, e mirim')

elif ano_final > 9 and ano_final <= 14:
  print(f'quem naceu em {ano} tem {ano_final} anos, e infantil')

elif ano_final > 14 and ano_final <= 19:
  print(f'quem naceu em {ano} tem {ano_final} anos, e junior')

elif ano_final > 19 and ano_final <= 25:
  print(f'quem naceu em {ano} tem {ano_final} anos, e senior')

else:
  print(f'quem naceu em {ano} tem {ano_final} anos, e master')