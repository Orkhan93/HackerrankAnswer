n=int(input())
for i in range(n):
    numbers=input()
    if (numbers.startswith("7") or numbers.startswith("8") or numbers.startswith("9")) and (len(numbers)==10 and numbers.isnumeric()) :
        print("YES")
    else:
        print("NO")
