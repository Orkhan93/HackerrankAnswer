eded01=int(input())
eded01list=list(map(int,input().split()))

eded02=int(input())
eded02list=list(map(int,input().split()))

eded01set=set(eded01list)
eded02set=set(eded02list)

new1=eded01set.difference(eded02set)
new2=eded02set.difference(eded01set)
new3=new1.union(new2)
newList=list(new3)
newList.sort()

for i in newList:
    print(i)
