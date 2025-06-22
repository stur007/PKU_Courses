s = []
stack = []
while True:
    try:
        str = input()
    except EOFError:
        break
    if 'push' in str:
        n = int(str[5:])
        s.append(n)
        if stack:
            stack.append(min(stack[-1], n))
        else:
            stack.append(n)
    elif 'pop' in str:
        if s:
            s.pop()
            stack.pop()
    elif 'min' in str:
        if s:
            print(stack[-1])
### 能够想到栈的思路，但是还是需要注意如何构建栈