from linkedlist import *

#Descripción: Agrega un elemento al comienzo de S, siendo S una
#estructura de tipo LinkedList
#Entrada: La pila S sobre la cual se quiere agregar el elemento
#(LinkedList) y el valor del elemento (element) a agregar.
#Salida: No hay salida definida
def push(S,element):
  add(S, element)
  return
#=====================================================================
#Descripción: extrae el primer elemento de la pila S, siendo S
#una estructura de tipo LinkedList
#Poscondición: Se debe desvincular el Node a eliminar.
#Entrada: la pila S (Linkedlist) sobre el cual se quiere realizar
#la eliminación
#Salida: Devuelve el elemento eliminado. Devuelve None si la pila
#está vacía.
def pop(S):
  largePila = length(S)
  if(largePila == 0):
    return None
  else:
    deleteNode = S.head.value
    S.head = S.head.nextNode
    return deleteNode
    
  