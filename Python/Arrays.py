import numpy

def arrays(arr):
    new_float_list=numpy.array(arr,float)
    reverse_list=new_float_list[::-1]
    return reverse_list

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
