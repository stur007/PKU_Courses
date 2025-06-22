n = int(input())
nums = []
while len(nums) < n*n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i*n:(i+1)*n])) for i in range(n)]
max_num = -float('inf')
for st in range(n):
    data = [0]*n
    for ed in range(st, n):
        for i in range(n):
            data[i] += matrix[ed][i]

        current_num = 0
        for i in range(n):
            current_num = max(current_num+data[i], data[i])
            max_num = max(current_num, max_num)
print(max_num)