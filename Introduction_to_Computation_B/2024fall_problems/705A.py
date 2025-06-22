a = 'I hate'
b = 'I love'
n = int(input())
ans = a
count = 1

while count < n :
    if count % 2 == 1:
        ans += ' that ' + b
    else:
        ans += ' that ' + a
    count += 1
ans += ' it'
print(ans)