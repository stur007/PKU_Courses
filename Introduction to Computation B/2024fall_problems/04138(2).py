def euler_sieve(n):
    is_prime = [True]*(n+1)
    primes = []
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
                if i*p > n:
                    break
                is_prime[i*p] = False
                if i%p == 0:
                    break
    return set(primes)
prime = euler_sieve(10000)
s = int(input())
for i in range(int(s/2),s+1):
    if (i in prime) and ((s-i) in prime):
        print(i*(s-i))
        break

### 由于运行的数字数量有限，用筛的方法和直接一个个判断的区别不大
