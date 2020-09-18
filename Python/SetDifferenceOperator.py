a=input()
first=set(map(int,input().split()))
b=input()
second=set(map(int,input().split()))

new_set=first.difference(second)

print(len(new_set))
