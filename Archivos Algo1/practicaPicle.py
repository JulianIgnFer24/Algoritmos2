import pickle
import binarytree


b = binarytree.BinaryTree()
binarytree.insert(b, 5,5)
binarytree.insert(b, 3,3)
binarytree.insert(b, 8,8)
binarytree.insert(b, 2,2)
binarytree.insert(b, 4,4)
binarytree.insert(b, 7,7)

with open("ArchivoTrie", 'wb') as archivo:
    pickle.dump(b, archivo)

with open("ArchivoTrie", 'rb') as archivo:
    b1 = pickle.load(archivo)

print(binarytree.search(b1, 3))
