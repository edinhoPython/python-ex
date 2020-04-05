soma = 0
comt = 0
for c in range(1,501,2):
  if c % 3 == 0:
    soma += c
    comt += 1
print(f'a soma de todos {comt} os valores solicitados e {soma}')