from itertools import permutations
myInput= list(map(str,input().upper().split()))

x=int(myInput[1])

a=myInput[0]
free=[]

for i in a:
    free.append(i)
free.sort()

lastList=list(permutations(free,x))
for i in lastList:
    print(*i,sep="")






