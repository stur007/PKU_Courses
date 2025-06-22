s = input()
dp = [[0]*len(s) for _ in range(len(s))]
for i in range(len(s)):
    dp[i][i] = 1
max_length = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 1
        max_length = 2
for length in range(3,len(s)+1):
    for i in range(len(s)-length+1):
        j = i +length -1
        if s[i] == s[j] and dp[i+1][j-1]:
            dp[i][j] = 1
            max_length = length
print(max_length)