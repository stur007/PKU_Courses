import math
while True:
    s = list(map(int, input().split()))
    if s == [0]*6:
        break
    strategy = 4*s[1]+9*s[2]+16*s[3]+25*s[4]+36*s[5]
    ans = 0
    ans += s[5]
    ans += s[4]
    ans += s[3]
    ans += math.ceil(s[2]/4)
    if s[1] > 5*s[3]:
        s[1] -= 5*s[3]
        if s[2]%4 == 1:
            s[1] -= 5
            if s[1] > 0:
                ans += math.ceil(s[1] / 9)
        elif s[2]%4 == 2:
            s[1] -= 3
            if s[1] > 0:
                ans += math.ceil(s[1] / 9)
        elif s[2] %4 == 3:
            s[1] -= 1
            if s[1] > 0:
                ans += math.ceil(s[1] / 9)
        else:
            if s[1] > 0:
                ans += math.ceil(s[1] / 9)

    if 36*ans-strategy >= s[0]:
        print(ans)
    else:
        s[0] -= 36*ans -strategy
        ans += math.ceil(s[0]/36)
        print(ans)
#**直接用总数把b c d e f占的位置都减掉就可以了，思路就清晰起来了。**运用列表，避免多个 if else。
'''
import math
rest = [0,5,3,1]

while True:
    a,b,c,d,e,f = map(int,input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = d + e + f           #装4*4, 5*5, 6*6
    boxes += math.ceil(c/4)     #填3*3
    space_for_b = 5*d + rest[c%4] #能和4*4 3*3 一起放的2*2
    if b > space_for_b:
    	boxes += math.ceil((b - space_for_b)/9)
    space_for_a = boxes*36 - (36*f + 25*e + 16*d + 9*c + 4*b)     #和其他箱子一起的填的1*1
    
    if a > space_for_a:
        boxes += math.ceil((a - space_for_a)/36)
    print(boxes)
'''