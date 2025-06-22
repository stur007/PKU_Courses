n, m = map(int, input().split())
island = [[(0,0)] * (m + 2)]
for _ in range(n):
    s = [(0,0)] + [(int(x),0) for x in input().split()] + [(0,0)]
    island.append(s)
island.append([(0,0)] * (m + 2))
for i in range(1,n+1):
    for j in range(1,m+1):
        if island[i][j][0] == 1:
            if island[i-1][j-1][0]+island[i-1][j][0]+island[i-1][j+1][0]+island[i][j-1][0]+island[i][j+1][0]+island[i+1][j-1][0]+island[i+1][j][0]+island[i+1][j+1][0] < 2:
                island[i][j] = (1,0)
            elif island[i-1][j-1][0]+island[i-1][j][0]+island[i-1][j+1][0]+island[i][j-1][0]+island[i][j+1][0]+island[i+1][j-1][0]+island[i+1][j][0]+island[i+1][j+1][0] > 3:
                island[i][j] = (1,0)
            else:
                island[i][j] = (1,1)
        else:
            if island[i-1][j-1][0]+island[i-1][j][0]+island[i-1][j+1][0]+island[i][j-1][0]+island[i][j+1][0]+island[i+1][j-1][0]+island[i+1][j][0]+island[i+1][j+1][0] == 3:
                island[i][j] = (0,1)
for k in range(1,n+1):
    print(' '.join(str(island[k][l][1]) for l in range(1,m+1)))