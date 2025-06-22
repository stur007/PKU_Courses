n = int(input())
store = 0
for _ in range(n):
    s = input().split()
    count = 0
    for i in range(len(s)-1):
        if '###' in s[i]:
            if '###' not in s[i+1]:
                count += 1

    if '###' in s[-1]:
        count += 1
    store += count
print(store)