import numpy

N, M=map(int,input().split())

# list_one=list(map(int,input().split()))
# list_two=list(map(int,input().split()))
# A=numpy.array([list_one for i in range(N)],int)
# B=numpy.array([list_two for i in range(N)],int)

A=numpy.array([list(map(int,input().split())) for i in range(N)],int)
B=numpy.array([list(map(int,input().split())) for i in range(N)],int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
