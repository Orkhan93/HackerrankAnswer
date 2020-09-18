cube = lambda x: x**3

def fibonacci_2(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_2(n-1) + fibonacci_2(n-2)

def fibonacci(n):
    arr=[]
    for i in range(n):
        arr.append(fibonacci_2(i))
    return arr
