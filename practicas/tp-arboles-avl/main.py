from avltree import *


B = AVLTree()

insert(B,"A",5)
insert(B,"B",2)
insert(B,"C",1)

#rotateLeft(B,B.root)

imprimir_arbol(B.root)
a=0
a = height(B.root)
print("la altura de B es: ",a)

calculateBalance(B)

print("los bf del arbol son")
print(B.root.bf)
print(B.root.leftnode.bf)
print(B.root.leftnode.leftnode.bf)