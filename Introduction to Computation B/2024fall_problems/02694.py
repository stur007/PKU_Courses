s = input().split()
def cal():
    char = s.pop(0)
    if char in '+-*/':
        return str(eval(cal() + char +cal()))
    else:
        return char
print('{:.6f}'.format(float(cal())))
