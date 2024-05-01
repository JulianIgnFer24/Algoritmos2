
def functionHash(k):
    hashnumber = k % 9
    return hashnumber
    
    
m = 1000
dictionary =[None] * 9

def insert(D, key, value):
    hashnumber = functionHash(key)
    if D[hashnumber] == None:
        D[hashnumber] = [(key,value)]
    else:
        D[hashnumber].append(key,value)


def search(D, key):
    hashnumber = functionHash(key)
    if D[hashnumber] == None:
        return None
    else:
        for i in range(len(D[hashnumber])):
            if D[hashnumber][i][0] == key:
                return D[hashnumber][i][1]
        return None

def delete(D,key):
    hashnumber = functionHash(key)
    if D[hashnumber] == None:
        return None
    else:
        for i in range(0,len(D[hashnumber])):
            if D[hashnumber][i][0] == key:
                D[hashnumber].pop(i)
                return
            

insert(dictionary, 1, "one")
insert(dictionary, 2, "two")
insert(dictionary, 3, "three")
insert(dictionary, 4, "four")




        
   
    
