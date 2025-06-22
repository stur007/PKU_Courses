ref = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
num = [1,5,10,50,100,500,1000]
s = input()
if s.isalpha():
    ans = 0
    for i in range(len(s)-1):
        if ref.index(s[i]) < ref.index(s[i+1]):
            ans -= num[ref.index(s[i])]
        else:
            ans += num[ref.index(s[i])]
    ans += num[ref.index(s[-1])]
    print(ans)
else:
    ans = ''
    s = s[::-1]
    for i in range(len(s)):
        num = int(s[i])
        if num <= 3:
            ans = ref[2*i]*num +ans
        elif num == 4:
            ans = ref[2*i]+ref[2*i+1] +ans
        elif num <= 8:
            ans = ref[2*i+1] + ref[2*i] *(num -5) + ans
        elif num == 9:
            ans = ref[2*i] + ref[2*i+2]+ ans
    print(ans)