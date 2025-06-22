from functools import lru_cache
import sys
sys.setrecursionlimit(1<<30)

def dfs_with_state(n, idx, fstline):
    global ans, cnt, target

    # 当 n == 1 时，检查是否满足条件
    if n == 1:
        cnt += sum(fstline)
        # print(f'cnt = {cnt}, target = {target}')
        if cnt == target:
            ans += 1
        cnt -= sum(fstline)  # 回溯时恢复 cnt 的状态
        return

    # 当 idx == n 时，生成下一行并递归
    if idx == n:
        cnt += sum(fstline)
        scdline = generate_next_line(fstline)  # 调用缓存的生成函数
        dfs_with_state(n - 1, n-1 , scdline)
        cnt -= sum(fstline)  # 回溯时恢复 cnt 的状态
        return

    # 尝试两种选择，递归
    for choice in [0, 1]:
        new_fstline = fstline[:idx] + (choice,) + fstline[idx + 1:]
        dfs_with_state(n, idx + 1, new_fstline)

@lru_cache(maxsize=None)
def generate_next_line(fstline):
    scdline = []
    for i in range(len(fstline) - 1):
        if fstline[i] == fstline[i + 1]:
            scdline.append(1)
        else:
            scdline.append(0)
    return tuple(scdline)

cheat = []
for n in range(1, 25):
    # 如果目标值不是整数，直接输出 0
    target = n * (n + 1) // 4
    if (n * (n + 1)) % 4 != 0:
        cheat.append(0)
    else:
        ans = 0
        cnt = 0
        fstline = tuple([0] * n)
        dfs_with_state(n, 0, fstline)
        cheat.append(ans)

print(cheat)
