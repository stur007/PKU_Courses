while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))
    except EOFError:
        break
    max_time = sum(s)/2
    s.sort()
    if s[-1] > max_time:
        t = sum(s)-s[-1]
        max_time = min(t, s[-1])
    print('%.1f' % max_time)

### 这个题目就是炸鸡排的变种，不是很难，但是需要有greedy的思维