t = int(input())
for _ in range(t):
    n, k = input().split()
    k = int(k)
    s = len(n)
    for _ in range(k):
        for i in range(len(n)):
            if i == len(n)-1:
                n = n[:-1]
                break
            if n[i] > n[i+1]:
                n = n[:i]+n[i+1:]
                break
    print(n)