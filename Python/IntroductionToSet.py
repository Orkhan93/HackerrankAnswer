def average(array):
    x=0
    new_arr=set(arr)
    for i in new_arr:
        x+=i
    average=x/len(new_arr)
    return average
