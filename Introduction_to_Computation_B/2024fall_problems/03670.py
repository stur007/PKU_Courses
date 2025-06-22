matrix=[[int(x) for x in input().split()] for _ in range(5)]
flag = 0
for i in range(5):
    a = max(matrix[i])
    if a == min(matrix[j][matrix[i].index(a)] for j in range(5)):
        print(str(i+1)+' '+str(matrix[i].index(a)+1)+' '+str(a))
        flag = 1
if not flag:
    print('not found')