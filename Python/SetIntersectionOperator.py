a=input()
first=set(map(int,input().split()))
b=input()
second=set(map(int,input().split()))

new_set=first.intersection(second)

print(len(new_set))
