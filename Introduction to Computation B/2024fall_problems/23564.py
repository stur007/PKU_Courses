def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact
factors = pFactors(int(input()))
counter = {x: factors.count(x) for x in factors}
exps = counter.values()
if len(exps) % 2 ==1:
    m = -1
else:
    m = 1
for exp in exps:
    if exp >= 2:
        m = 0
        break
print(m)