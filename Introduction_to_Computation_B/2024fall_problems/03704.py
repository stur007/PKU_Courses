while True:
    try:
        s = input()
    except EOFError:
        break
    left = []
    right = []

    for i in range(len(s)):
        if s[i] == '(':
            left.append(i)
        elif s[i] == ')':
            if left:
                left.pop()
            else:
                right.append(i)
        else:
                continue

    ans=[' ']*len(s)
    for number in left:
        ans[number]='$'
    for number in right:
        ans[number]='?'
    print(*ans,sep='')