def ajuda(com):
    titulo(f'acessando o manual de \"{com}\"')
    help(com)

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    titulo('Sistema ajuda pyhelp')
    comando = str(input('comando ou bliblioteca > '))

    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)

titulo('ate logo')