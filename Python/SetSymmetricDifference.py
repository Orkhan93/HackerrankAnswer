a=input()
first=set(map(int,input().split()))
b=input()
second=set(map(int,input().split()))

new_set=first.difference(second)
new_set2=second.difference(first)
new_set3=new_set.union(new_set2)
print(len(new_set3))
