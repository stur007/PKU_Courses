while True:
    try:
        s = input()
    except EOFError:
        break
    if s == s[::-1]:
        print('YES')
    else:
        print('NO')
