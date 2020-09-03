n = int(input())
arr=list()
x=0
a=None
for i in range(n):
    a = int(input())
    arr.append(a)
for b in arr:
    x = x + b
print(x)
