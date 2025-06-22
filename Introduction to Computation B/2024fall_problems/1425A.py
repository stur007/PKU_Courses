"""t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    clct = 0
    while n>0:
        cnt += 1
        if n%2 == 0:
            temp = n//2
            n = n//2
        else:
            temp = 1
            n -= 1
        if cnt %2 == 1:
            clct += temp
    print(clct)"""
#第一次完成这个题目的时候没有意识到这个题目原来不仅仅是超时这么简单，还要考虑最优解的问题
import sys
input = sys.stdin.read

def solve(n):
    f = s = 0  # To distinguish between first and second hands.
    fs = True

    if n & 1:
        n -= 1
        fs = False

    while n:
        if n == 4:
            f += 3
            s += 1
            n = 0  # Special case
        elif (n // 2) & 1:  # The First Situation
            f += n // 2
            s += 1
            n = (n // 2) - 1
        else:  # The Second Situation
            f += 1
            s += 1
            n -= 2
    ans.append([s + 1, f][fs])

data = input().split()
t = int(data[0])
coins = list(map(int, data[1:t + 1]))

ans = []
for i in coins:
    if i == 1:
        ans.append(1)
    else:
        solve(i)

print('\n'.join(map(str, ans)))
### 这段代码过于极限了，实测用时2000ms整，然后发现实在是太容易超时了，这个题目非常有趣