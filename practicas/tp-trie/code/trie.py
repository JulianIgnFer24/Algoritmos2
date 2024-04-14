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
insert(T,"OLA")
insert(T,"OJALA")
print_trie(T.root)
print(len("HOLA"))
#print(T.root.children[0].children[0].children[0].children[0].isEndOfWord)
#--------------------------------------------------------

        