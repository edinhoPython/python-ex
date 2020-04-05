def metade(P, R=False):
    val = P / 2
    if R:
        val = str(val).replace('.', ',')
        return f'R$ {val}0'
    else:
        return val

def dobro(P, R=False):
    val = P * 2
    if R:
        val = str(val).replace('.', ',')
        return f'R$ {val}0'
    else:
        return val

def aumento(P, V, R=False):
    val = (P * V) / 100
    if R:
        val = str(val).replace('.', ',')
        return f'R$ {val}0'
    else:
        return val

def desconto(P, V, R=False):
    val = (P * V) / 100
    if R:
        val = str(val).replace('.', ',')
        return f'R$ {val}0'
    else:
        return val

def moeda(P):
    return f'R$ {P:.2f}'