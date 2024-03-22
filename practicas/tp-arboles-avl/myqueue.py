from linkedlist import *


#Descripción: Agrega un elemento al comienzo de Q, siendo Q una
#estructura de tipo LinkedList.
#Entrada: La cola Q (LinkedList) sobre la cual se quiere agregar
#el elemento y el valor del elemento (element) a agregar.
#Salida: No hay salida definida.
def enqueue(Q, element):
  add(Q, element)
  return


#Descripción: extrae el último elemento de la cola Q, siendo Q
#una estructura de tipo LinkedList.
#Poscondición: Se debe desvincular el Node a eliminar.
#Entrada: la cola Q (Linkedlist) sobre el cual se quiere realizar
#la eliminación.
#Salida: Devuelve el elemento de la cola. Devuelve None si la
#cola está vacía.
def dequeue(Q):
  largeCola = length(Q)
  if (largeCola == 0):
    return None
  else:
    currentNode = Q.head
    for j in range(0, largeCola - 1):
      currentNode = currentNode.nextNode
    value = currentNode.value
    current = Q.head
    for i in range(0, largeCola - 2):
      current = current.nextNode
    current.nextNode = None

    return (value)
