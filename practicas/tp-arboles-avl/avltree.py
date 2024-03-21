class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

#rota a la izquierda
def rotateLeft(Tree, avlnode):
  nodeAnt = avlnode
  parentAnt = avlnode.parent
  newRoot = avlnode.rightnode

  if newRoot.leftnode == None:
    nodeAnt.parent = newRoot
    newRoot.leftnode = nodeAnt
    if nodeAnt.parent != Tree.root:
      newRoot.parent = parentAnt
    else:
      Tree.root = newRoot

  return (newRoot)

#rota a la derecha
def rotateRight(Tree, avlnode):
  nodeAnt = avlnode
  parentAnt = avlnode.parent
  newRoot = avlnode.leftnode

  if newRoot.rightnode == None:
    if nodeAnt.parent == newRoot:
      newRoot.rightnode = nodeAnt
      if nodeAnt.parent != Tree.root:
        newRoot.parent = parentAnt
      else:
        Tree.root = newRoot

    return (newRoot)

#calcula la altura desde un nodo dado
def heigth(node):
  if node is None:
    return 0

  left = heigth(node.leftnode)
  right = heigth(node.rightnode)

  if left >= right:
    return left + 1
  else:
    return right + 1

''' Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.
Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None. '''


def insert(B, element, key):
  newNode = AVLNode()
  newNode.key = key
  newNode.value = element
  newNode.bf = 0 

  if (B.root == None):
    B.root = newNode
    return key
  return insertR(newNode, B.root)


# Función recursiva de insert
def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      newNode.parent = currentNode
      currentNode.rightnode = newNode
      return newNode.key
    else:
      right = insertR(newNode, currentNode.rightnode)
      if right != None:
        return right
  else:
    if currentNode.leftnode == None:
      newNode.parent = currentNode
      currentNode.leftnode = newNode
      return newNode.key
    else:
      left = insertR(newNode, currentNode.leftnode)
      if left != None:
        return left

