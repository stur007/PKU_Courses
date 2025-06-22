n , q = map(int, input().split())
s = []
flag = 0
for _ in range(q):
    x, y = map(int, input().split())
    s.append([x, y])
for k in s:
    j = list(reversed(k))
    if j in s:
        flag = 1
        break
if flag:
    print('Yes')
else:
    print('No')

###学会了使用reversed()函数，然后下面是答案中的做法，个人认为并不是特别好。
'''
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    
    exists = [[False] * (n + 1) for _ in range(n + 1)]  # 初始化喜欢关系矩阵
    result = False  # 是否存在双向喜欢的情况
    
    index = 2
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        exists[a][b] = True  # a喜欢b
        if exists[b][a]:  # 如果b也喜欢a，则存在双向喜欢
            result = True
    
    print("Yes" if result else "No")

if __name__ == "__main__":
    main()
    '''