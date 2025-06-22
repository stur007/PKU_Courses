r_a,c_a = [int(x) for x in input().split()]
matrix_a = [[int(y) for y in input().split()] for _ in range(r_a)]
r_b,c_b = [int(x) for x in input().split()]
matrix_b = [[int(y) for y in input().split()] for _ in range(r_b)]
r_c,c_c = [int(x) for x in input().split()]
matrix_c = [[int(y) for y in input().split()] for _ in range(r_c)]
if c_a != r_b:
    print('Error!')
else:
    matrix_ab = [[0]*c_b for z in range(r_a)]
    for i in range(r_a):
        for j in range(c_b):
            for k in range(c_a):
                matrix_ab[i][j] += matrix_a[i][k]*matrix_b[k][j]
    matrix_ans = [[0]*c_b for z in range(r_a)]
    if r_a == r_c and c_b == c_c:
        for a in range(r_a):
            for b in range(c_b):
                matrix_ans[a][b] = matrix_ab[a][b]+ matrix_c[a][b]
        for _ in range(r_c):
            print(*matrix_ans[_],sep =' ')
    else:
        print('Error!')
