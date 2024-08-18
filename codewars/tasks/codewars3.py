#Currying functions: multiply all elements in an array

def multiply_all(r):
    def multiply(n):
        listn = []
        for i in range(0, len(r)):
            mul = r[i] * n
            listn.append(mul)
        return listn
    return multiply