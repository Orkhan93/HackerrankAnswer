n=list(map(int,input().split()))

def minimum_remove(n):
    x=0
    n=sorted(n)
    n.remove(n[0])
    for i in n:
        x+=i
    return x

def maximum_remove(n):
    x=0
    n=sorted(n)
    n.remove(n[-1])
    for i in n:
        x+=i
    return x

print(maximum_remove(n),minimum_remove(n))
