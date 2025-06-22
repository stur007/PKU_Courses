from bisect import bisect_left
data = []
current_len = 0
sum_len = 0
for i in range(1,4*10**4):
    current_len += len(str(i))
    sum_len += current_len
    data.append(sum_len)
'''if data[-1] > 2147483647:
    print('yes')
else:
    print('no')'''
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else: ### 一开始使用了break指令，然后发现竟然直接跳出了循环，一定要注意代码的逻辑
        """for i in range(1,4*10**4):
            if data[i-1] < n <= data[i]:
                n -= data[i-1]
                break"""
        i = bisect_left(data, n)
        n -= data[i-1]
        ### 思考， 此处能否使用二分查找呢
        ### 事实是，确实得到了一定的优化（97ms->84ms)
        for k in range(1,i+2):
            if n > len(str(k)):
                n -= len(str(k))
            else:
                break
        search = str(k)
        print(search[n-1])
