m ,n = map(int, input().split())
s = list(map(int, input().split()))

ans = 1
collection = set()

for i in range(len(s)):
    collection.add(s[i])
    if len(collection) == n:
        ans += 1
        collection.clear()

print(ans)

### 第一次半独立做出greedy题目，感觉非常好！！！