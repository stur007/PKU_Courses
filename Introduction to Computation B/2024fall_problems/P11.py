for i in range(5):
    line=input().split()
    if '1' in line:
        print(abs(i-2)+abs(line.index('1')-2))
        break