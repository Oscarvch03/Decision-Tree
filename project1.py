class Arbol:
    def nodo(rotulo, Intervalo, iz , der):
        
        Arbol = nodo("A", A1, A2)
        A1 = nodo("A1",[0,0.5], A11, A12) 
        A11 = nodo("A11",[0,0.25), null, null)
        A12 = nodo("A12",[0.25,0.5], null, null)
        A2 = nodo("A2",[0.5,1], A21, A22)
        A21 = nodo("A21",[0.5,0.75], null, null)
        A22 = nodo("A22", [0.75,1], null, null)

    for
#_____________________________________________________________________________

#ARBOL
class nodo:
    izq, der, info, key, intervalo = None, None, None, None, [0,1] 

    def _init_ (self, info):
        self.izq = None
        self.der = None
        self.info = info

class arbolBinario:

    def _init_(self):
        self.raiz = None

    def agregarNodo(info):
        return nodo(info)

    

#OPERACIONES
    def insertar(self, raiz, info):
        if raiz == None:
            return self.agregarNodo(info)
        else:
            if info < raiz.info:
                raiz.izq = self.insertar(raiz.izq, info)
            else:
                raiz.der = self.insertar(raiz.der, info)
            return raiz

    def buscar(raiz, key):
        if raiz == None:
            print "No se encontro el dato"
        else:
            if key == raiz.info:
                print "La informacion " + dato + "se encuentra en el rotulo" + key
            elif key < raiz.info:
                return buscar(raiz.izq, key)
            else:
                return buscar(raiz.der, key)

#Nota: Definir las variables de instancia

    
 

    

   

    

    
    
    

    

    
