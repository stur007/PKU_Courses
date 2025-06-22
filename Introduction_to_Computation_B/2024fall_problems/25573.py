s = input()
if s[0] == 'R':
    dp1 = [0]
    dp2 = [1]
else:
    dp1 = [1]
    dp2 = [0]
for i in range(1, len(s)):
    if s[i] == 'R':
        dp1.append(min(dp1[-1], dp2[-1]+1))
        dp2.append(min(dp1[-1]+1, dp2[-1]+1))
    else:
        dp1.append(min(dp1[-1]+1, dp2[-1]+1))
        dp2.append(min(dp2[-1], dp1[-1]+1))
print(dp1[-1])