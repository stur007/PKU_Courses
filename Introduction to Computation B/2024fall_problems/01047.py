while True:
    try:
        s = input()
    except EOFError:
        break
    n = len(s)
    digit = int(s)
    num = 2*digit
    ref = '0'*(n-len(str(num)))+str(num)
    flag = 0
    for i in range(n):
        ref = ref[-1]+ref[:-1]
        if ref == s:
            flag = 1
            break
    if flag:
        print(f'{s} is cyclic')
    else:
        print(f'{s} is not cyclic')