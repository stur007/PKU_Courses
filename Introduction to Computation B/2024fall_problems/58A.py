s = input()
target='hello'
index=0

for char in s:
    if char == target[index]:
        index+=1
        if index == 5 :
            break

if index == 5 :
    print('YES')
else:
    print('NO')