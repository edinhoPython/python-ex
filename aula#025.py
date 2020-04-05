nome = str(input('qual seu nome conpleto ').upper()).split()

tem = False

for p in nome:
    if p == 'SILVA':
        tem = True

    else:
        tem = False

print(f'seu nome tem silva ? {tem}')