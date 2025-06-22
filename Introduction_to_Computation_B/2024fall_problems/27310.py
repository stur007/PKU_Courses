n = int(input())
ref = []
for _ in range(4):
    ref.append(input())

def dfs(s, i, temp, used, ans):
    if i == len(s):
        if len(temp) == len(s):
            ans.append(temp[:])
            return
    for idx in range(4):
            if s[i] in ref[idx] and not used[idx]:
                temp.append(idx)
                used[idx] = True
                dfs(s, i+1, temp, used, ans)
                used[idx] = False
                temp.pop()

for _ in range(n):
     a = input()
     ans = []
     dfs(a, 0, [], [False]*4, ans)
     if ans:
         print('YES')
     else:
         print('NO')
