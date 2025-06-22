def f(n,x,y):
    if n > 1:
        if x =='a' and y == 'c':
            return f(n-1,'a','b')+f'\n{n}:{x}->{y}\n'+f(n-1,'b','c')
        elif x == 'a' and y == 'b':
            return f(n-1,'a','c')+f'\n{n}:{x}->{y}\n'+f(n-1,'c','b')
        elif x == 'b' and y == 'c':
            return f(n-1,'b','a')+f'\n{n}:{x}->{y}\n'+f(n-1,'a','c')
        elif x == 'b' and y == 'a':
            return f(n-1,'b','c')+f'\n{n}:{x}->{y}\n'+f(n-1,'c','a')
        elif x == 'c' and y == 'a':
            return f(n-1,'c','b')+f'\n{n}:{x}->{y}\n'+f(n-1,'b','a')
        else:
            return f(n-1,'c','a')+f'\n{n}:{x}->{y}\n'+f(n-1,'a','b')
    else:
        return f'{n}:{x}->{y}'
s = input().split()
print(f(int(s[0]),s[1],s[3]))
