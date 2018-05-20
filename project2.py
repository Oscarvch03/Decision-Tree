######################################################################################

#Librerias Importadas

import random
import matplotlib.pyplot as plt

######################################################################################

# Definir los objetos arboles

class Tree(object):
    def __init__(self, izq, der, rotulo, intervalo):
        self.izq = izq
        self.der = der
        self.rotulo = rotulo
        self.intervalo = intervalo

######################################################################################

# Definir las funciones

def crear_objetos(NoObjetos):

    # Crea objetos (numeros flotantes) al azar entre 0 y 1, y los inserta
    # En una lista

    objetos = []
    for i in range(NoObjetos):
        objetos.append(random.uniform(0,1))
    return objetos


def crear_contexto(NoObjetos, TamContexto):

    # Selecciona objetos a partir de la lista Objetos
    # devuelve una lista nueva con los objetos seleccionados

    return random.sample(NoObjetos, TamContexto)

def buscar(nodo, valor):

    # Revisa que rotulo se le asigna a un objeto

    print "Buscando en categoria: " + str(nodo.rotulo) + " con el valor: " + str(valor)
    if nodo.izq != None:
        if (valor > nodo.izq.intervalo[0]) and (valor < nodo.izq.intervalo[1]):
             print "Chinga la cosa a la izquierda"
             return buscar(nodo.izq, valor)
        else:
            print "Ay caramba"
            if nodo.der != None:
                if (valor > nodo.der.intervalo[0]) and (valor < nodo.der.intervalo[1]):
                     print "Chinga la cosa a la derecha"
                     return buscar(nodo.der, valor)
                else:
                     print "Ay caramba, estamos en la mala"
    else:
        print "Lo que buscas es: " + str(nodo.rotulo)
        return nodo.rotulo

def insertar(nodo, valor):

    # Inserta los objetos seleccionados en la funcion crear_contexto, clasificandolos
    # en el arbol de discriminacion

    if nodo.izq != None:
        if (valor > nodo.izq.intervalo[0]) and (valor < nodo.izq.intervalo[1]):
            print "Esta a la izq"
            return Tree(insertar(nodo.izq, valor), nodo.der, nodo.rotulo, nodo.intervalo)
        else:
            print "Esta a la der"
            return Tree(nodo.izq, insertar(nodo.der, valor), nodo.rotulo, nodo.intervalo)
    else:
        print "En el nodo " + str(nodo.rotulo) + " insertamos dos nodos"
        nodo.izq = Tree(None, None, nodo.rotulo + "1", [nodo.intervalo[0], (nodo.intervalo[0] + nodo.intervalo[1]) /2])
        nodo.der = Tree(None, None, nodo.rotulo + "2", [(nodo.intervalo[0] + nodo.intervalo [1])/2 , nodo.intervalo[1]])
        return nodo

def juego_discriminacion(nodo, Contexto):

    # Recibe un arbol y una lista de cinco objetos (contexto) y devuelve True si el rotulo
    # de contexto[0] es diferente del rotulo de los demas objetos del contexto. Devuelve
    # False en otro caso.

    print "El contexto es: ", Contexto
    rotulos = []
    for o in Contexto:
        rotulos.append(buscar(nodo, o))

    print "Los rotulos son: ", rotulos
    if rotulos[0] in rotulos[1:]:
        print "No lo se Rick, parece falso"
        return False

    else:
        print "Si es real, Podria valer una fortuna"
        return True

def Rondas_100(Ronda, Objetos):

    # Ejecuta la funcion juego_discriminacion determinadas veces para evaluar la eficiencia
    # de aprendizaje del arbol de discriminacion
    # Si la maquina gana (es decir logra asignarle un rotulo a un unico objeto), entonces al
    # contador Heroe se le suma 1
    # Si la maquina pierde (es decir se le asigna mas de un objeto a un rotulo), entonces al
    # contador Asistente se le suma 1
    # A la vez el estado actual por ronda de cada contador se agrega a una lista respectiva,
    # y el ultimo numero de cada lista es la cantidad de veces que la maquina gano y perdio

    Heroe = 0
    Asistente = 0
    victorias = []
    derrotas = []

    A = Tree(None, None, "A", [0.,1.])

    for n in range(Ronda):
        contexto = crear_contexto(Objetos, TamContexto)
        print "Vamos a correr el juego con el arbol: ", imprimir_arbol(A)
        if juego_discriminacion(A, contexto):
            Heroe += 1
        else:
            A = insertar(A, contexto[0])
            Asistente += 1
        victorias.append(Heroe)
        derrotas.append(Asistente)
    return A, victorias, derrotas

def imprimir_arbol(A):

    # Imprime el arbol de cada ronda de juego_discriminacion en notacion [ [] [] ]

    if A.izq == None:
        return str(A.rotulo)
    else:
        return "[" + imprimir_arbol(A.izq) + ", " + imprimir_arbol(A.der) + "]"

######################################################################################

# PARAMETROS DEL MODELO

# NoObjetos: Los objetos del mundo con los cuales se arman los contextos
# TamContexto: Los objetos seleccionados al azar de la lista de NoObjetos
# Ronda: cantidad de rondas para jugar el juego de discriminacion

NoObjetos = 10
TamContexto = 3
Ronda = 10

######################################################################################

# Invocar las funciones principales

Objetos = crear_objetos(NoObjetos)
print Objetos

Arb, vict , derr = Rondas_100(Ronda, Objetos)

# Imprimir el porcentaje de veces que la maquina perdio o gano el juego

print vict
print "El porcentaje de victorias es: " + str(float(vict[-1])/Ronda*100) + "%"
print derr
print "El porcentaje de derrotas es: " + str(float(derr[-1])/Ronda*100) + "%"

######################################################################################

# Graficas (Rondas ganadas vs Total Rondas) && (Rondas perdidas vs Total Rondas)

a, b = plt.subplots()
b.set_ylabel('Victorias Acumuladas')
b.set_xlabel('Ronda')
b.plot(vict)

plt.hold(True)

c, d = plt.subplots()
d.set_ylabel('Derrotas Acumuladas')
d.set_xlabel('Ronda')
d.plot(derr)

plt.show()

######################################################################################
