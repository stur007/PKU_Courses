t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(y) for y in input().split()]
    print(min(min(a)*n+sum(b),min(b)*n+sum(a)))
