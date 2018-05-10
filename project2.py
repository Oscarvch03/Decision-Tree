# -*- coding: utf-8 -*-

import random 

#####################################
##### Definicion de objetos y clases

# Define los objetos arboles

class Tree(object):
    def __init__(self, izq, der, rotulo, intervalo):
        self.izq = izq
        self.der = der
        self.rotulo = rotulo
        self.intervalo = intervalo

# OPERACIONES
##def insertar(Arbol, valor):
    # Divide en dos el nodo mas pequenho que clasifica valor
    # Mira si nodo.izq != None:
    # si si, revisar si valor esta en el intervalo de nodo.izq o nodo.der
    # dependiendo de esto, correr insertar (nodo.izq, valor) o insertar(nodo.der, valor)
    # Mirar si nodo.izq == None
    # Si sí:
    # nodo.izq(None, None, nodo.rotulo + "1", [nodo.intervalo[0], ?????])
    # nodo.der(None, None, nodo.rotulo + "2", [?????, nodo.intervalo[1]])
    ##return nodo

def crear_objetos(NoObjetos):
    # for i in range("NoObjetos"):
    #   anhadir a la lista un objeto aleatorio
    objetos = []
    for i in range(NoObjetos):
        objetos.append(random.uniform(0,1))
    return objetos
    #depende del numero de objetos


def buscar(nodo, valor):
    print "Buscando en categoria: " + str(nodo.rotulo)
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


def crear_contexto(objetos, longitud):
    # Selecciona cinco objetos a partir de la lista Objetos
    # Se sobreentiende que el primer objeto sera el foco
    # devuelve una lista de objetos
    return random.sample(objetos, longitud)


def juego_discriminacion(Arbol, contexto):
    # Recibe un arbol y una lista de cinco objetos (contexto)
    # y devuelve True si el rotulo de contexto[0] es diferente
    # del rotulo de los demas objetos del contexto. Devuelve
    # False en otro caso.
    print "El contexto es: ", contexto
    rotulos = []
    for o in contexto:
        rotulos.append(buscar(Arbol, o))

    print "Los rotulos son: ", rotulos
    if rotulos[0] in rotulos[1:]:
        print "Ouch, si esta"




###############################
# PARAMETROS DEL MODELO
NoObjetos = 20
TamContexto = 5
###############################

Objetos = crear_objetos(NoObjetos)
print Objetos

Contexto = crear_contexto(Objetos, TamContexto)
print Contexto




# Ejemplo de un arbolBinario

A11 = Tree(None, None, "A11", [0, 0.25])
A12 = Tree(None, None, "A12", [0.25, 0.5])
A1 = Tree(A11, A12, "A1", [0, 0.5])
A2 = Tree(None, None, "A2", [0.5, 1])
A = Tree(A1, A2, "A", [0, 1])

# A = (None, None, "A", [0, 1])
# A = insertar(A)
# A.izq = insertar(A.izq)


Juego = juego_discriminacion(A, Contexto)
print Juego

