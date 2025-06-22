s_len = [0]
n = int(input())
temp_len = [0]
temp = ''
for i in range(1,4*10**4):
    temp += str(i)
    temp_len.append(len(temp))
    s_len.append(s_len[-1]+len(temp))
    if s_len[-1] > n:
        break
    i -= 1
    n -= s_len[-2]