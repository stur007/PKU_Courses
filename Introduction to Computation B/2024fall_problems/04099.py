m = int(input())
for _ in range(m):
    flag = 1
    n = int(input())
    queue = []
    stack = []
    for _ in range(n):
        s = input()
        if 'push' in s:
            char = int(s[5:])
            queue.append(char)
            stack.append(char)
        else:
            if not queue:
                flag = 0
            else:
                queue.pop(0)
            if not stack:
                flag = 0
            else:
                stack.pop(-1)
    if flag:
        print(*queue)
        print(*stack)
    else:
        print('error')
        print('error')