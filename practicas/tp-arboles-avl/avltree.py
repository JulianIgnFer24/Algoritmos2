class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

def rotateLeft(Tree, avlnode):
  newRoot = avlnode.rightnode

  if newRoot.leftnode == None:
    if avlnode != Tree.root:
      avlnode.parent = newRoot
    else:
      Tree.root = newRoot
    avlnode.rightnode = None
    newRoot.leftnode = avlnode

  return (newRoot)

#rota a la derecha YA ANDA BIEN
def rotateRight(Tree, avlnode):
  newRoot = avlnode.leftnode

  if newRoot.rightnode == None:
    if avlnode != Tree.root:
      avlnode.parent = newRoot
    else:
      Tree.root = newRoot
    avlnode.leftnode = None
    newRoot.rightnode = avlnode

  return (newRoot)

#calcula la altura desde un nodo dado
def height(node):
  if node is None:
      return -1  # Base para nodos vacíos, -1 para que la raíz sea 0
  else:
    height_left = height(node.leftnode)
    height_right = height(node.rightnode)
    return max(height_left, height_right)+1


#lleno los Bf recursivamente 
def BFrecursive(node):
  if node != None:
    BFrecursive(node.leftnode)
    BFrecursive(node.rightnode)
    node.bf = heigth(node.leftnode)-heigth(node.rightnode)
#calcula el bf de cada nodo de un AVL
def calculateBalance(AVLTree):
  if AVLTree == None:
    return(None)
  else:
    return(BFrecursive(AVLTree))





def imprimir_arbol(node, prefix="", is_left=True):
    if node.rightnode:
        imprimir_arbol(node.rightnode, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    if node.leftnode:
        imprimir_arbol(node.leftnode, prefix + ("    " if is_left else "│   "), True)







''' Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.'''
'''Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None. '''
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

