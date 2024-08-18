#The Vowel Code

def encode(st):
    listn = []
    all = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    
    for i in st:
        if i in all:
            listn.append(all[i])
        else:
            listn.append(i)
    return "".join(listn)
    
    
    
    
def decode(st):
    listn = []
    all = {"1":"a","2":"e","3":"i","4":"o","5":"u"}
    
    for i in st:
        if i in all:
            listn.append(all[i])
        else:
            listn.append(i)  
    return "".join(listn)