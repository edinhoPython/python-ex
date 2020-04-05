
from random import randint
numeros = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],[25],[26],[27],[28],[29],[30],[31],[32],[33],[34],[35],[36],[37],[38],[39],[40]]

vezes = int(input('quantas vezes '))
final = []

for cont in range(1,vezes + 1):
  final = []
  for cont1 in range(1,7):
    num = randint(0,len(numeros))
    if num not in final:
      final.append(num)
    
  print(final)