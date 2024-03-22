from avltree import *
def imprimir_arbol(node, prefix="", is_left=True):
    if node is None:
        return  # Condición de salida para nodos vacíos
    if node.rightnode != None:
        imprimir_arbol(node.rightnode, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    if node.leftnode != None:
        imprimir_arbol(node.leftnode, prefix + ("    " if is_left else "│   "), True)

# Asegúrate de que esta función esté definida en el mismo ámbito que la instancia de tu árbol AVL.


B = AVLTree()

insert(B,"A",5)
insert(B,"B",2)
insert(B,"C",7)

imprimir_arbol(B.root)

rotateLeft(B,B.root)

print("arbol rotado a la IZQUIERDA")
#imprimir_arbol(B.root)
imprimir_arbol(B.root)
# print("arbol rotado a la izquierda (deberia ser el original)")
# rotateLeft(B,B.root)
# imprimir_arbol(B.root)