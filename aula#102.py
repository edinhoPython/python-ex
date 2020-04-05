def fatorial(n,show=False):
  print('-' * 25)
  if show == False:
    f = n
    while n != 1:
      f *= n -1 
      n -= 1
  
  if show == True:
    for c in range(n, 0, -1):
      if c == 1:
        print(f'1 = ',end='')
      else:
        print(f'{c} x ',end='')
    f = n
    while n != 1:
      f *= n -1 
      n -= 1
  
  return f
  
    

print(fatorial(5, True))