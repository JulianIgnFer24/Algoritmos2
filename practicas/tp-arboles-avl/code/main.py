from avltree import *


B = AVLTree()

insert(B,"A",5)
insert(B,"B",3)
insert(B,"C",6)
insert(B,"D",7)
insert(B,"E",8)
calculateBalance(B)
print("peimera impresion del arbol original")
imprimir_arbol(B.root)
reBalance(B)

# a=0
# a = height(B.root)
# print("la altura de B es: ",a)
#rotateRight(B,B.root)
# calculateBalance(B)
#rotateLeft(B,B.root)
print("ARBOL BALANCEADO")
imprimir_arbol(B.root)
# print("arbol rotado a la izquierda del segundo nodo")
# rotateLeft(B,B.root.rightnode)
# imprimir_arbol(B.root)
# print("el padre del nodo rotado es: ", B.root.rightnode.parent.key)


# rotateRight(B,B.root.rightnode)
# print("arbol rotado a la derecha del segundo nodo")
# imprimir_arbol(B.root)
# #print(B.root.rightnode.rightnode.parent.key)
# # print("los bf del arbol son")
# # print(B.root.rightnode.bf)
# # print(B.root.leftnode.bf)
# print(B.root.rightnode.rightnode)