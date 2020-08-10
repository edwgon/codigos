def a(cualquier_parametro):
    """
    Descripcion general
    cualquier_parametro int cualquier entero
    returns cualquier_ parametro + 5
    """
    return cualquier_parametro +5
#help(a)

#Recursividad
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)
#n = int(input("Ingrese Numero"))
#print(factorial(n))
cantidad_numeros = int(input("Cuantos números quieres que tenga la sucesión de fibonacci "))
serie = [1,1]
inicial = 0
final = 1
largo = len(serie)
print(serie[0])
print(serie[1])
while cantidad_numeros > largo:
    x = serie[inicial]+serie[final]
    serie.append(x)
    inicial+=1
    final+=1
    largo = len(serie)
    print(x)

#tuplas
my_tuple=()
print(id(my_tuple))
my_tuple=(1,"dos",True)
print(id(my_tuple))
my_tuple[0]
my_tuple[1]
my_tuple =(1)
type(my_tuple)
my_tuple =(1,)
type(my_tuple)
my_other_tuple = (2,3,4)
my_tuple= my_tuple + my_other_tuple
print(id(my_tuple))
print(my_tuple)
x,y,z,a = my_tuple
print(x)
print(a)

#rangos
comienzo =5
termina=9
pasos=1
my_range=range(comienzo,termina,pasos)
for i in my_range:
    print(i)

#Direccion en memoria
u = id(my_tuple)
d= id(my_range)
print(my_tuple is my_other_tuple)
print(f'tupla {u}\nrango{d}\n')

#Listas
my_list=[1,2,3]
print(id(my_list))
my_list[0]
print(my_list[1:])
print(id(my_list))
my_list.append(4)
print(id(my_list))
print(my_list)
my_list[0] = "a"
print(id(my_list))
print(my_list)
my_list.pop()
print(id(my_list))
print(my_list)
for element in  my_list:
    print(element)
a=["a","b","c"]
uno = [1,2,3]
b = a
print(a)
print(id(a))
print(b)
print(id(b))
c= [a,b]
print(c)
print(id(c))
a.append(5)
print(c)
print(id(c))
c.append(5)
print(c)
print(id(c))
a =[1,2,3]
print(a)
print(id(a))
d = a[::]
print(d)
print(id(d))
a.append(5)
print(a)
print(id(a))
print(d)
print(id(d))

d = list(a)
print(d)
print(id(d))
a.append(5)
print(a)
print(id(a))
print(d)
print(id(d))

#list comprehension
lista = list(range(100))
print(lista)
doble = [i*2 for i in lista]
print(doble)
pares = [i for i in lista if i %2 ==0]
print(pares)
#diccionarios
diccionario = {'david':32,'erika' : 34,'jaime':50}
print(diccionario['david'])
diccionario['jaime'] = 80
print(diccionario)
del diccionario['jaime']
print(diccionario)
diccionario['carlos'] = 80
print(diccionario)
for llave in diccionario.keys():
    print(llave)
for valor in diccionario.values():
    print(valor)
for llave,valor in diccionario.items():
    print(f'llave{llave}:valor{valor}')
print('david' in diccionario)
print('oscar' in diccionario)
#si la mitad de la edad es par 
edades = {'Juan': 3, 'Juliana': 21, 'Carlos': 33, 'Valentina': 60, 'Oscar': 55,'Johana':26}
edades_mitad_par = { k:v/2 for (k,v) in edades.items() if v % 2 == 0}
print(edades_mitad_par)
