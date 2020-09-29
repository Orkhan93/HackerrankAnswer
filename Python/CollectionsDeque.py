from collections import deque
number=int(input())
d = deque()
for i in range(number):
    myInput=list(map(str,input().split()))
    if myInput[0].lower()=="append":
        d.append(int(myInput[1]))
    if myInput[0].lower()=="appendleft":
        d.appendleft(int(myInput[1]))
    if myInput[0].lower()=="pop":
        d.pop()
    if myInput[0].lower()=="popleft":
        d.popleft()
print(*d)



