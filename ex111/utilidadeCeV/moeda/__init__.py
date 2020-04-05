def dobro(V):
    resul = V * 2
    return resul

def metade(V):
    resul = V / 2
    return resul

def aumento(V, P):
    resul = V + (V * P) / 100
    return resul

def desconto(V, P):
    resul = V - (V * P) / 100
    return resul

def linha():
    print('=' * 38)

def desenha(msg, v):
    tam_msg = len(msg)
    e = 30 - tam_msg
    print(f'{msg}', end='')
    print(' ' * e, end='')
    print(f'R${v:.2f}'.replace('.', ','))

def resulmo(V, PA=10, PD=10):
    R = [dobro(V), metade(V), aumento(V, PA), desconto(V, PD)]
    
    linha()
    print(f'{"resulmo do valor":>26}')
    linha()
    desenha('analize do valor', V)
    desenha('o dobro e:', R[0])
    desenha('a metade:', R[1])
    desenha(f'aumento de {PA}%:', R[2])
    desenha(f'desconto de {PD}%:', R[3])
    linha()
