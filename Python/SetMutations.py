n=int(input())
mySet=set(map(int,input().split()))

loopNumber=int(input())
for i in range(loopNumber):
    myInput=list(map(str,input().split()))
    if myInput[0].lower()=="intersection_update":
        mySet.intersection_update(set(map(int,input().split())))

    if myInput[0].lower()=="update":
        mySet.update(set(map(int,input().split())))

    if myInput[0].lower()=="symmetric_difference_update":
        mySet.symmetric_difference_update(set(map(int,input().split())))

    if myInput[0].lower()=="difference_update":
        mySet.difference_update(set(map(int,input().split())))

print(sum(mySet))



