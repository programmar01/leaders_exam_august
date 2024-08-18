#Reverse every other word in the string

def reverse_alternate(string):
    result = []
    arr = string.split()
    for i in arr:
        if arr.index(i) % 2 == 1:
            result.append(arr[arr.index(i)][::-1])
        
        else:
            result.append(arr[arr.index(i)])
        
    return " ".join(result)