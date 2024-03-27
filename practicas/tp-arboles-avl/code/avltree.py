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
  newRoot = avlnode.rightnode
  avlnode.rightnode = newRoot.leftnode


  if newRoot.leftnode != None:
      newRoot.leftnode.parent = avlnode
  newRoot.parent = avlnode.parent


  if avlnode.parent == None:
      Tree.root = newRoot
  else:
      if avlnode.parent.leftnode == avlnode:
          avlnode.parent.leftnode = newRoot
      else:
          avlnode.parent.rightnode = newRoot
  newRoot.leftnode = avlnode
  avlnode.parent = newRoot

  return(newRoot)

#rota a la derecha
def rotateRight(Tree, avlnode):
  newRoot = avlnode.leftnode
  avlnode.leftnode = newRoot.rightnode

  if newRoot.rightnode != None:
      newRoot.rightnode.parent = avlnode
  newRoot.parent = avlnode.parent


  if avlnode.parent == None:
      Tree.root = newRoot
  else:
      if avlnode.parent.rightnode == avlnode:
          avlnode.parent.rightnode = newRoot
      else:
          avlnode.parent.leftnode = newRoot
  newRoot.rightnode = avlnode
  avlnode.parent = newRoot
  return(newRoot)
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
  altNodo = height(node)
  if altNodo != 0:
    node.bf = height(node.leftnode)-height(node.rightnode)
  else:
    node.bf = 0
  if node.leftnode != None:
    BFrecursive(node.leftnode)
  if node.rightnode != None:
    BFrecursive(node.rightnode)
    
#calcula el bf de cada nodo de un AVL
def calculateBalance(AVLTree):
  if AVLTree == None:
    return(None)
  else:
    return(BFrecursive(AVLTree.root))

#imprime un arbol binario, hay que pasar la raiz
def imprimir_arbol(node, prefix="", is_left=True):
    if node is None:
        return  # Condición de salida para nodos vacíos
    if node.rightnode != None:
        imprimir_arbol(node.rightnode, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    if node.leftnode != None:
        imprimir_arbol(node.leftnode, prefix + ("    " if is_left else "│   "), True)

#funcion que balancea un arbol recursivamente
def recursiveBalance(node,Tree):
  if node == None:
    return
  if node.bf == 2: #caso para cuando hay que girar a la derecha
    if node.rightnode != None:
      if node.rightnode.bf == -1:
        rotateLeft(Tree,node.leftnode)
    rotateRight(Tree,node)
  if node.bf == -2: #caso para cuando hay que girar a la izqiuerda
    if node.rightnode != None:
      if node.rightnode.bf == 1:
        print("entra a el if que tiene un hijo izquierdo")
        rotateRight(Tree,node.rightnode)
    rotateLeft(Tree,node)
  recursiveBalance(node.leftnode,Tree)
  recursiveBalance(node.rightnode,Tree)


#balancea un arbol binario de busqueda 
def reBalance(AVLTree):
  if AVLTree == None:
    return None
  else:
    return(recursiveBalance(AVLTree.root,AVLTree))

#inserta un nodo en un arbol binario hay que modificarlo para que sea avl 
def insert(B, element, key):
  newNode = AVLNode()
  newNode.key = key
  newNode.value = element
  newNode.bf = 0 

  if (B.root == None):
    B.root = newNode
    return key
  insertR(newNode, B.root)
  return(reBalance(B))

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

#funcion que elimina un nodo de un arbol binario    
def deleteKey(B, key):
  node = searchKeyR(B.root, key)
  if node == None: return
  else:
    deleteCurrentCase(B, node)
    calculateBalance(B)
    return reBalance(B)

# Devuelve el elemento con mayor key desde un nodo dado
def bigger(node):
  if node.rightnode != None:
    current = bigger(node.rightnode)
    if current != None:
      return current
  else:
    return node

#busca un nodo por su key
def searchKey(B, key):
  node = searchKeyR(B.root, key)
# Función recursiva de searchKey
def searchKeyR(node, key):
  if node == None: return

  if node.key == key:
    return node

  right = searchKeyR(node.rightnode, key)
  if right != None:
    return right

  left = searchKeyR(node.leftnode, key)
  if left != None:
    return left
#elimina segun el caso del nodo
def deleteCurrentCase(B, node):
  if node.rightnode == None:
    if node.leftnode == None:

      # Caso 1: El nodo a eliminar es una hoja
      if node.parent.leftnode != None and node.parent.leftnode == node:
        node.parent.leftnode = None
        return node.key
      elif node.parent.rightnode != None and node.parent.rightnode == node:
        node.parent.rightnode = None
        return node.key

    # Caso 2: El nodo a eliminar tiene un hijo del lado izquierdo
    if node.parent.leftnode != None and node.parent.leftnode == node:
      node.parent.leftnode = node.leftnode
      return node.key
    elif node.parent.rightnode != None and node.parent.rightnode == node:
      node.parent.rightnode = node.leftnode
      return node.key

  else:
    # Caso 2: El nodo a eliminar tiene un hijo del lado derecho
    if node.leftnode == None:
      if node.parent.leftnode == node:
        node.parent.leftnode = node.rightnode
        return node.key
      elif node.parent.rightnode == node:
        node.parent.rightnode = node.rightnode
        return node.key
    else:
      # Caso 3: El nodo a eliminar tiene dos hijos'

      # o eliminar el mayor de sus menores
      changeNode = bigger(node.leftnode)

      node.value = changeNode.value
      oldKey = node.key
      node.key = changeNode.key

      if changeNode.parent.leftnode == changeNode:
        changeNode.parent.leftnode = None
      elif changeNode.parent.rightnode == changeNode:
        changeNode.parent.rightnode = None

      return oldKey