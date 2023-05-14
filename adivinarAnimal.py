'''
    importamos los módulos necesarios para trabajar con archivos binarios ademas de verificar si un archivo existe en la ruta.
'''
from pickle import dump, load
from os.path import isfile


class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def escribe_dato(fichero, dato):
    '''
    Escribe cualquier dato en el archivo binario indicado por 
    fichero.
    '''
    with open(fichero,'wb') as archivo:
        dump(dato, archivo)


def lee_dato(archivo):
    '''
    Lee cualquier dato contenido en el archivo binario indicado por
    nombre_archivo.
    '''
    with open(archivo,'rb') as archivo:
        return load(archivo)
     
def obtener_respuesta(pregunta):
    ''' Aqui se proporciona una pregunta como parametro de entrada a lo que se debe proporcionar una respuesta de S o N de forma que si la respuesta no es S ni N mostrara un texto "respuesta invalida" '''
    respuesta = input(pregunta + " (s/n): ")
    while respuesta.lower() != "s" and respuesta.lower() != "n":
        respuesta = input("Respuesta inválida. " + pregunta + " (s/n): ")
    return respuesta.lower()


def adivinar_animal(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        respuesta = obtener_respuesta("¿Es un(a) " + nodo.valor + "?")
        if respuesta == "s":
            print("BIEN,ACERTE!!!")
        else:
            nuevo_animal = input("No sé qué animal es. ¿En qué animal estabas pensando?: ")
            pregunta = input("Escribe una pregunta que sea verdadera para un/a " + nuevo_animal +
                             " pero falsa para un/a " + nodo.valor + ": ")
            respuesta_nueva_pregunta = obtener_respuesta("Para  un/a  " + nuevo_animal + ", " + pregunta)
            if respuesta_nueva_pregunta == "s":
                nodo.derecha = Nodo(nuevo_animal)
                nodo.izquierda = Nodo(nodo.valor)
            else:
                nodo.derecha = Nodo(nodo.valor)
                nodo.izquierda = Nodo(nuevo_animal)
            nodo.valor = pregunta
    else:
        respuesta = obtener_respuesta(nodo.valor)
        if respuesta == "s":
            adivinar_animal(nodo.derecha)
        else:
            adivinar_animal(nodo.izquierda)
            

if isfile('arbol.bin'):
    arbol = lee_dato('arbol.bin')
else:
    
    arbol = Nodo("Es animal terrestre?")
    arbol = Nodo("Vive en el agua?")
    
    arbol.derecha = Nodo("pez")
    arbol.izquierda = Nodo("perro")
    

adivinar_animal(arbol)

jugar_nuevamente = obtener_respuesta("¿Deseas jugar otra vez?")
while jugar_nuevamente == "s":
    adivinar_animal(arbol)
    jugar_nuevamente = obtener_respuesta("¿Deseas jugar otra vez?")

escribe_dato('arbol.bin', arbol)
print("Adiós.") 