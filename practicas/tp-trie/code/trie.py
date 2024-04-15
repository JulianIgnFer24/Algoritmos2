class Trie:
	root = None

class TrieNode:
    parent = None   #padre
    children = None   #cabecera  de  una lista
    key = None #aca va la letra
    isEndOfWord = False #si es el final de una palabra

#--------------------------------------------------------
#function that serches letter in list
def searchCharacter(list,letter):
      for i in range(len(list)):
            if list[i].key == letter:
                return(i)
      else:
            return None


def insert(T, element):
    if T.root is None:
        T.root = TrieNode()
        T.root.children = []
    final = False
    currentNode = T.root
    for i in range(len(element)):
        lst = currentNode.children
        posInList = searchCharacter(lst, element[i])
        if i == len(element)-1:
            final = True
        if posInList is not None:
            currentNode = lst[posInList]
        else:
            newNode = TrieNode()
            newNode.key = element[i]
            newNode.parent = currentNode
            newNode.children = []
            lst.append(newNode)
            if final:
                newNode.isEndOfWord = True
            currentNode = newNode

#--------------------------------------------------------

#function that serches words in the trai
def search(T,element):
    currentNode = T.root
    for i in range(len(element)):
        a = searchCharacter(currentNode.children,element[i])
        if  i == len(element)-1 and a != None and currentNode.children[a].isEndOfWord == True:
            return  True
            
        if a == None or i == len(element)-1:
            return False
        else:
            currentNode = currentNode.children[a]
        
#--------------------------------------------------------

def delete(T,element):
    if search(T,element) == False:
        return  False
    else:
        currentNode = T.root
        for i in range(len(element)):
            #con las siguientes dos lineas me voy hasta el ultimo nodo de la palabra
            a = searchCharacter(currentNode.children,element[i])
            currentNode = currentNode.children[a]
        currentNode.isEndOfWord = False #hacemos que en la ultima letra de la palabla ya no sea endWord
        
        if len(currentNode.children) != 0: #nos fijamos si hay mas letras para abajo
            return True
        cont = 0
        seDivide = False
        while seDivide == False:
            currentNode = currentNode.parent
            cont = cont+1
            if  len(currentNode.children) > 1 or currentNode.isEndOfWord == True:
                seDivide = True
        
        pos = searchCharacter(currentNode.children,element[len(element)-cont])
        del currentNode.children[pos]


#--------------------------------------------------------
#print the trie
def print_trie(node, level=0):
    if node is None:
        return
    print('    ' * level, end='')
    if node.key is not None:
        print(node.key)
    for child in node.children:
        print_trie(child,level+1)

T = Trie()
insert(T,"HOLA")
insert(T,"HOLANDA")
insert(T,"OLA")
insert(T,"OJALA")
print_trie(T.root)
#print(T.root.children[0].children[0].children[0].children[0].parent.key)
print("---------------------------------------")
delete(T,"HOLANDA")
print_trie(T.root)

#--------------------------------------------------------
#a = T.root.children[0].children[0].children[0].children[0].parent.children[0]
#print(a.parent.parent.parent.parent.key)

        