range_number=int(input())
for i in range(range_number):
    set_length_one, A=input(), set(input().split())
    set_length_two, B=input(), set(input().split())
    z=A.issubset(B)
    print(z)
