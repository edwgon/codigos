import random ,math


def media(x):
    return sum(x)/len(x)

def varianza(x):
    mu = media(x)
    acumulador = 0
    for X in x:
        acumulador += (X - mu)**2

    return acumulador

def desviacion_estandar(x):
    return math.sqrt(varianza(x))


if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)
    print(f'Arreglo de x es {X}')
    print(f'Media es: {mu}')
    print(f'Varianza es: {Var}')
    print(f'Desviacion Estandar es: {sigma}')