n=int(input())
for i in range(n):
    try:
        a,b=input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as x:
        print("Error Code:",x)
    except ValueError as x:
        print("Error Code:",x)
