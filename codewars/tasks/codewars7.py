#Going to zero or to infinity?

def going(n):
    first = 1
    second = 0
    for i in range(1, n + 1):
        first *= i
        second += first
    
    return second/first