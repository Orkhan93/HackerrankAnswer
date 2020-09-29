from itertools import combinations_with_replacement
myInput= list(map(str,input().upper().split()))

x=int(myInput[1])

a=myInput[0]
free=[]

for i in a:
    free.append(i)
free.sort()

lastList=list(combinations_with_replacement(free,x))
for i in lastList:
    print(*i,sep="")




