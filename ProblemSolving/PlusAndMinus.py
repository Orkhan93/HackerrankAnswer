x=0
arrNegative=[]
arrZero=[]
arrPositive=[]

n=int(input())
numbers=list(map(int,input().split()))
for i in numbers:
    if i<0:
        arrNegative.append(i)
    elif i==0:
        arrZero.append(i)
    else:
        arrPositive.append(i)
print(f"{round(len(arrPositive)/n,6):2f}")
print(f"{round(len(arrNegative)/n,6):2f}")
print(f"{round(len(arrZero)/n,6):2f}")
