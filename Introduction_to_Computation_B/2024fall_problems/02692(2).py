n = int(input())
for _ in range(n):
    d, e, f = set('ABCDEFGHIJKL'), set('ABCDEFGHIJKL'), set()
    for j in range(3):
        a, b, c = input().split()
        if c == 'even':
            f = f | set(a + b)
        elif c == 'up':
            d = d & set(b)
            e = e & set(a)
        else:
            d = d & set(a)
            e = e & set(b)
    g = d & f
    h = e & f
    e = e - h
    d = d - g
    if d:
        s = list(d)[0]
        print('{} is the counterfeit coin and it is light.'.format(s))
        continue
    s = list(e)[0]
    print('{} is the counterfeit coin and it is heavy.'.format(s))

# This kind of solution can be fun to learn! (with the use of set)