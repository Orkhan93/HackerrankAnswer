commanNumber=int(input())
freeList=[]
for i in range(commanNumber):
    myInput=list(map(str,input().split()))
    if myInput[0]=="insert":
        freeList.insert(int(myInput[1]),int(myInput[2]))
    if myInput[0]=="print":
        print(freeList)
    if myInput[0]=="remove":
        freeList.remove(int(myInput[1]))
    if myInput[0]=="append":
        freeList.append(int(myInput[1]))
    if myInput[0]=="sort":
        freeList.sort()
    if myInput[0]=="pop":
        freeList.pop()
    if myInput[0]=="reverse":
        freeList.reverse()


