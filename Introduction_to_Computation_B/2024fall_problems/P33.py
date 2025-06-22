n = int(input())
for ans in range(1,n+1):
    if n % ans == 0 and ans >= 6:
        print(int(n//ans))
        break