from operator import add, sub, mul
from functools import reduce

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '^': lambda x, y: x ** y,
    '!': lambda z: reduce(lambda x, y: x*y, range(1, z+1)),
    '?': lambda z: reduce(lambda x, y: x+y, range(1, z+1))
}


def avaliador(expressao):
    valores = expressao.split()
    numeros = []

    for elemento in valores:
        if elemento.isdigit():
            numeros.append(int(elemento))
        else:
            x = numeros.pop()
            if elemento == '!' or elemento == '?':
                numeros.append(operacoes[elemento](x))
                return numeros[0]
            y = numeros.pop()
            numeros.append(operacoes[elemento](y, x))

    return numeros[0]
