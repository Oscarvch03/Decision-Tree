# -*- coding: utf-8 -*-
# class Arbol:
#     def nodo(rotulo, Intervalo, iz , der):
#
#         Arbol = nodo("A", A1, A2)
#         A1 = nodo("A1",[0,0.5], A11, A12)
#         A11 = nodo("A11",[0,0.25), null, null)
#         A12 = nodo("A12",[0.25,0.5], null, null)
#         A2 = nodo("A2",[0.5,1], A21, A22)
#         A21 = nodo("A21",[0.5,0.75], null, null)
#         A22 = nodo("A22", [0.75,1], null, null)
#
#     for
# #_____________________________________________________________________________

#ARBOL
# Define los objetos arboles
class Tree(object):
    def __init__(self, iz, der, rotulo, intervalo):
        self.izq = iz
        self.der = der
        self.rotulo = rotulo
        self.intervalo = intervalo

# OPERACIONES
def insertar(Arbol, valor):
    # Divide en dos el nodo mas pequenho que clasifica valor
    # Mira si nodo.izq != None:
    # si si, revisar si valor esta en el intervalo de nodo.izq o nodo.der
    # dependiendo de esto, correr insertar (nodo.izq, valor) o insertar(nodo.der, valor)
    # Mirar si nodo.izq == None
    # Si sí:
    # nodo.izq(None, None, nodo.rotulo + "1", [nodo.intervalo[0], ?????])
    # nodo.der(None, None, nodo.rotulo + "2", [?????, nodo.intervalo[1]])
    return nodo

def crear_objetos(NoObjetos):
    objetos = []
    # for i in range(NoObjetos):
    #   anhadir a la lista un objeto aleatorio

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

def crear_contexto(Objetos):
    # Selecciona cinco objetos a partir de la lista Objetos
    # Se sobreentiende que el primer objeto sera el foco
    # devuelve una lista de objetos

def juego_discriminacion(Arbol, contexto):
    # Recibe un arbol y una lista de cinco objetos (contexto)
    #

#Nota: Definir las variables de instancia

# Ejemplo de un arbolBinario

A11 = Tree(None, None, "A11", [0, 0.25])
A12 = Tree(None, None, "A12", [0.25, 0.5])
A1 = Tree(A11, A12, "A1", [0, 0.5])
A2 = Tree(None, None, "A2", [0.5, 1])
A = Tree(A1, A2, "A", [0, 1])

# A = (None, None, "A", [0, 1])
# A = insertar(A)
# A.izq = insertar(A.izq)

cat = buscar(A, 0.3)
print cat
