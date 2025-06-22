"""while True:
    n = int(input())
    if n == 0:
        break
    s= list(map(int,input().split()))
    s.sort(reverse = True)
    tot_length = sum(s)
    for per_tot in range(s[0], tot_length+1):
        if tot_length % per_tot == 0:
            i = tot_length//per_tot
            test = [0] *i
            visited = set()

            def f(idx):
                if idx == len(s):
                    return sum(test) == tot_length
                for j in range(len(test)):
                    if j > 0 and test[j] == test[j - 1]:
                        continue
                    if test[j] + s[idx] <= per_tot:
                        test[j] += s[idx]
                        if tuple(sorted(test)) in visited:
                            test[j] -= s[idx]
                            return
                        else:
                            visited.add(tuple(sorted(test)))
                            if f(idx + 1):
                                visited.clear()
                                return True
                            test[j] -= s[idx]
                return False
            if f(0):
                print(per_tot)
                break"""

"""from functools import lru_cache

while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    tot_length = sum(s)

    for per_tot in range(s[0], tot_length + 1):
        if tot_length % per_tot == 0:
            i = tot_length // per_tot


            @lru_cache(maxsize = 8192)  ## 尝试了一下是可行的
            def f(idx, test):
                if idx == len(s):
                    return all(x == per_tot for x in test)

                for j in range(len(test)):
                    if j > 0 and test[j] == test[j - 1]:
                        continue
                    if test[j] + s[idx] <= per_tot:
                        next_test = list(test)
                        next_test[j] += s[idx]
                        next_test = tuple(sorted(next_test))
                        if f(idx + 1, next_test):
                            return True
                return False


            initial_test = tuple([0] * i)
            if f(0, initial_test):
                print(per_tot)
                break"""

### 发现答案的剪枝更强，佩服！
def dfs(unused, left, len):
    if unused == 0 and left == 0:
        return True
    if left == 0:
        left = len

    for i in range(N):
        if used[i] == False and length[i] <= left:
            if i > 0:
                if used[i - 1] == False and length[i] == length[i - 1]:
                    continue  # 不要在同一个位置多次尝试相同长度的木棒，剪枝1

            used[i] = True
            if dfs(unused - 1, left - length[i], len):
                return True
            used[i] = False

            # 不能仅仅通过替换最后一根木棒来达到目的，剪枝3
            # 替换第一个根棍子是没有用的，因为就算现在不用，也总会用到这根木棍，剪枝2

            # 如果我们进行尝试的时候，所使用的这根木棍长度恰好与为达到给定长度所需要的长度相等
            # （也就是说使用了这根木棍就可以开始新尝试），
            # 亦或此时恰好开始一次新的尝试，得到的结果是False，那么就说明这个给定长度不满足条件。
            if length[i] == left or left == len:
                break

    return False


while True:
    N = int(input())
    if N == 0:
        break

    length = [int(x) for x in input().split()]
    length.sort(reverse=True)  # 排序是为了从长到短拿木棒进行尝试

    totalLen = sum(length)

    for L in range(length[0], totalLen // 2 + 1):
        if totalLen % L:
            continue  # 不是木棒长度和的因子的长度，直接否定

        used = [False] * 65
        if dfs(N, 0, L):
            print(L)
            break
    else:
        print(totalLen)