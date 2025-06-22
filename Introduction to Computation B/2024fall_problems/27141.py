# 只能是说没有看懂题目的意思，还是自己的问题
n = int(input())
s = list(map(int, input().split()))
for i in range(n):
    s[i] -= 520
current_pre = dict()
pre = 0
max_length = 0
for i in range(n):
    pre += s[i]
    if pre in current_pre:
        if pre == 0:
            max_length = max(max_length, i-current_pre[pre]+1)
        else:
            max_length= max(max_length, i- current_pre[pre])
    else:
        current_pre[pre] = i
print(max_length*520)

# 看懂了以后还是挺简单的，就是求连续的和为零的字符串长度，有点像dp的味道，但是还是要难想一点，和CF2033D还是有点像