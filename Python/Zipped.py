firts_inputs=list(map(int,input().split()))

students , list_num = firts_inputs[0] , firts_inputs[1]

my_list=[]

for i in range(list_num):
    qiymetler=list(map(float,input().split()))
    my_list.append(qiymetler)


for i in zip(*my_list):
    i=list(i)
    print(sum(i)/list_num)
