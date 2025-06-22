x = int(input())
while True:
    if x%2 ==1:
        y = int(x*3 +1)
        print(f'{x}*3+1={y}')
        x = y
    else:
        y = int(x/2)
        print(f'{x}/2={y}')
        x = y
    if x == 1:
        break
