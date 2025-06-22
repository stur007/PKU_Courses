weights = [1, 2, 3, 5, 10, 20]


def dfs(index, cur_w):
	# 已尝试所有可能砝码，递归结束
    if index == 6:
        if cur_w != 0:
            w.add(cur_w)
        return
    #遍历所有可能的使用该砝码个数
    for i in range(max_w[index]+1):
        dfs(index+1, cur_w+i*weights[index])


max_w = list(map(int, input().split()))
#使用set自动去重
w = set()
dfs(0, 0)
print(f'Total={len(w)}')