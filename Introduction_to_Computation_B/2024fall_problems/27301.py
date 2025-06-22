n, a, b = map(int,input().split())
s = list(map(int,input().split()))
current_a, current_b, i, j ,cnt= a, b, 0 ,n-1, 0

while i<j:
    if current_a < s[i]:
        cnt += 1
    current_a = a
    current_a -= s[i]

    i += 1
    if current_b < s[j]:
        cnt += 1
        current_b = b
    current_b -= s[j]
    j -= 1

if i == j and max(current_b,current_a) < s[i]:
    cnt +=1
print(cnt)

### 自我感觉本题疑似出错，感觉不满足题目条件，就是Alice和Bob的水瓶足够大能够一次浇完所有植物，尤其是处理边界条件的时候