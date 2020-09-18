import numpy

first_arr=list(map(int,input().split()))
second_arr=list(map(int,input().split()))

print(numpy.inner(first_arr,second_arr))
print(numpy.outer(first_arr,second_arr))
