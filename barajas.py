import random, collections

PALOS = ['espada','corazon','rombo','trebol']
VALORES =['as','2','3','4','5','6','7','8','9','10','J','Q','K']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas

def obtener_mano(barajas,tamano_mano):
    mano = random.sample(barajas,tamano_mano)
    return mano

def main(tamano_mano,intentos):
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas,tamano_mano)
        manos.append(mano)
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        print(counter)
        for val in counter.values():
            if val == 3:
                pares += 1
                break
    probabilidad_par = pares /intentos
    print(f'Probabilidad de encrontrar pares es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano =  int(input('Cuantas barajas'))
    intentos =  int(input('Cuantos intentos'))
    manos = main(tamano_mano,intentos)
    print(f'Resultado ->')