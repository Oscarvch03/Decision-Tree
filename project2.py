# -*- coding: utf-8 -*-
######################################################################################

#Librerias Importadas

import random
import matplotlib.pyplot as plt

######################################################################################
##### Definicion de objetos y Funciones

# Define los objetos arboles

class Tree(object):
    def __init__(self, izq, der, rotulo, intervalo):
        self.izq = izq
        self.der = der
        self.rotulo = rotulo
        self.intervalo = intervalo

def imprimir_arbol(A):
    # Imprime un arbol en notacion [ [] [] ]
    if A.izq == None:
        return str(A.rotulo)
    else:
        return "[" + imprimir_arbol(A.izq) + ", " + imprimir_arbol(A.der) + "]"

def insertar(nodo, valor):
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


def crear_objetos(NoObjetos):
    # for i in range("NoObjetos"):
    #   anhadir a la lista un objeto aleatorio
    objetos = []
    for i in range(NoObjetos):
        objetos.append(random.uniform(0,1))
    return objetos
    #depende del numero de objetos


def buscar(nodo, valor):
    # print "Buscando en categoria: " + str(nodo.rotulo) + " con el valor: " + str(valor)
    if nodo.izq != None:
        if (valor > nodo.izq.intervalo[0]) and (valor < nodo.izq.intervalo[1]):
             # print "Chinga la cosa a la izquierda"
             return buscar(nodo.izq, valor)
        else:
            # print "Ay caramba"
            if nodo.der != None:
                if (valor > nodo.der.intervalo[0]) and (valor < nodo.der.intervalo[1]):
                     # print "Chinga la cosa a la derecha"
                     return buscar(nodo.der, valor)
                # else:
                #     print "Ay caramba, estamos en la mala"
    else:
        # print "Lo que buscas es: " + str(nodo.rotulo)
        return nodo.rotulo


def crear_contexto(NoObjetos, TamContexto):
    # Selecciona cinco objetos a partir de la lista Objetos
    # Se sobreentiende que el primer objeto sera el foco
    # devuelve una lista de objetos
    return random.sample(NoObjetos, TamContexto)


def juego_discriminacion(nodo, Contexto):
    # Recibe un arbol y una lista de cinco objetos (contexto)
    # y devuelve True si el rotulo de contexto[0] es diferente
    # del rotulo de los demas objetos del contexto. Devuelve
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
    # Ronda: cantidad de rondas para jugar el juego de discriminacion
    # Objetos: Los objetos del mundo con los cuales se arman los contextos
    #
    Heroe = 0
    victorias = []
    A = Tree(None, None, "A", [0.,1.])
    for n in range(Ronda):
        contexto = crear_contexto(Objetos, TamContexto)
        print "Vamos a correr el juego con el arbol: ", imprimir_arbol(A)
        if juego_discriminacion(A, contexto):
            Heroe += 1
        else:
            A = insertar(A, contexto[0])

        victorias.append(Heroe)
    return A, victorias

######################################################################################


# Ejemplo de un arbolBinario
# Nodos
# A222 = Tree(None, None, "A222",[0.875, 1])
# A221 = Tree(None, None, "A221",[0.75, 0.875])
#
# A212 = Tree(None, None, "A212",[0.625, 0.75])
# A211 = Tree(None, None, "A211",[0.5, 0.625])
#
# A122 = Tree(None, None, "A122",[0.375, 0.5])
# A121 = Tree(None, None, "A121",[0.25, 0.375])
#
# A112 = Tree(None, None, "A112",[0.125, 0.25])
# A111 = Tree(None, None, "A111",[0, 0.125])
#
# A22 = Tree(A221, A222, "A22",[0.75, 1])
# A21 = Tree(A211, A212, "A21",[0.5, 0.75])
#
# A12 = Tree(A121, A122, "A12",[0.25, 0.5])
# A11 = Tree(A111, A112, "A11",[0, 0.25])
#
# A12 = Tree(None, None, "A12",[0.25, 0.5])
# A11 = Tree(None, None, "A11",[0, 0.25])
#
# A22 = Tree(None, None, "A22",[0.75, 1])
# A21 = Tree(None, None, "A21",[0.5, 0.75])
#
# A2 = Tree(A21, A22, "A2",[0.5, 1])
# A1 = Tree(A11, A12, "A1",[0, 0.5])
#
# A = Tree(A1, A2, "A", [0, 1])
#
# print imprimir_arbol(A)

# A = (None, None, "A", [0, 1])
# A = insertar(A)
# A.izq = insertar(A.izq)


######################################################################################

# PARAMETROS DEL MODELO
NoObjetos = 20
TamContexto = 5
Ronda = 100

######################################################################################

# Invocar Funciones

# Buscar = buscar(A, 0.3)
# print Buscar
#
# ##Insertar = insertar(A, 0.3)
# ##print Insertar
#
Objetos = crear_objetos(NoObjetos)
print Objetos


Arb, Succ = Rondas_100(Ronda, Objetos)
print Succ
print "El porcentaje de victorias es: " + str(float(Succ[-1])/Ronda*100) + "%"


f, axarr = plt.subplots(1)
axarr.set_ylabel('Victorias Acumuladas')
axarr.set_xlabel('Ronda')
axarr.plot(Succ)
plt.show()
