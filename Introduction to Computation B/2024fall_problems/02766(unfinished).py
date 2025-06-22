m, n = map(int,(input()).split())
nums = []

matrix = [list(map(int, input().split())) for _ in range(m)]
maxv = 0
for i in range(m):
        left_side = [0]*n
        right_side = [0]*n

        left_stack = []
        right_stack = []

        height = []
        for j in range(n):
            h = 0
            for k in range(i, m):
                if matrix[k][j] == 0:
                    h += 1
                else:
                    height.append(h)
                    break
                if k == m-1:
                    height.append(h)
        for j in range(n):
                h = height[j]
                while left_stack and matrix[i][left_stack[-1]] > h:
                    idx = left_stack.pop()
                    left_side[idx] = j-idx
                left_stack.append(j)

        height.reverse()
        for j in range(n):
                h = height[j]
                while right_stack and matrix[i][right_stack[-1]] > h:
                    idx = right_stack.pop()
                    right_side[idx] = j-idx
                right_stack.append(j)
        height.reverse()
        right_side.reverse()
        for j in range(n):
            maxv = max(maxv, height[j]*(left_side[j]+right_side[j]+1))

print(maxv)