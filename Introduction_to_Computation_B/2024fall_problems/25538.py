n = int(input())
y = int(bin(n)[2:][::-1],2)
if n == y:
    print('Yes')
else:
    print('No')