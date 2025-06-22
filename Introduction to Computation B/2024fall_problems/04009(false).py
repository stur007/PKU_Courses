import sys
sys.setrecursionlimit(1<<30)
from functools import lru_cache
from collections import Counter

def find1(s):
    a = 0
    for i in s:
        if i == '1':
            a += 1
    return a

@lru_cache(maxsize= None)
def cnt(n):
    if n == 1:
        return {'1':1, '0':0}
    adict = {}
    for s in cnt(n-1).keys():
        ss1 = s+'1'
        ss1_r = ''
        for i in range(1, len(ss1)):
            if ss1[i] == ss1[i-1]:
                ss1_r += '1'
            else:
                ss1_r += '0'
        adict[ss1] = find1(ss1)+cnt(n-1)[ss1_r]
        ss2 = s+'0'
        ss2_r = ''
        for i in range(1, len(ss2)):
            if ss2[i] == ss2[i-1]:
                ss2_r+= '1'
            else:
                ss2_r+= '0'
        adict[ss2] = find1(ss2)+cnt(n-1)[ss2_r]

    return adict

cheat = {}
for n in range(1, 16):
    ans = list(cnt(n).values())
    ref = Counter(ans)
    most_common = ref.most_common(1)
    most_common_cnt = most_common[0][1]
    if most_common_cnt == 1:
        cheat[n] = most_common_cnt-1
    else:
        cheat[n] = most_common_cnt - 1

print(cheat)

### 显然这种方法是超时超内存的