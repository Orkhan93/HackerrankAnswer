import numpy


first_arr=list(map(float,input().split()))
second_arr=list(map(float,input().split()))

print(float(numpy.polyval(first_arr,second_arr)))
