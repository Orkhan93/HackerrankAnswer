n = int(input())
s = set(map(int, input().split()))
forNumber=int(input())
for i in range(forNumber):
    myInput=list(map(str,input().split()))
    if myInput[0].lower()=="pop":
        s.pop()
    if myInput[0].lower()=="remove":
        s.remove(int(myInput[1]))
    if myInput[0].lower()=="discard":
        s.discard(int(myInput[1]))
print(sum(s))

