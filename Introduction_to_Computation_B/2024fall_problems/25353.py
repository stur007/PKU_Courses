n, d = map(int, input().split())
h = []
for _ in range(n):
    h.append(int(input()))
current = 0
option = [float('inf'), 0]
ans = []
while len(h):
    for i in range(len(h)):
        current = max(current, h[i])
        if current - h[i] <= d:
            if option[0] >= h[i]:
                option = [h[i], i]
    ans.append(h[option[1]])
    h.pop(option[1])
    current = 0
    option = [float('inf'), 0]
print(*ans, sep = '\n')