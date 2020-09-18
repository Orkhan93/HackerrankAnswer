from itertools import product

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))

for i in list(product(n1,n2)):
    print(i,end=" ")
