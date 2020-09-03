n = int(input(" : "))
a=[]
for i in range(n):
    x=int(input(" : "))
    a.append(x)
print(*a)
# a.reverse()
print(*a[::-1])

