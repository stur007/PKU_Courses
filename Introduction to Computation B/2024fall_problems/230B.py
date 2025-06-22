import math


def euler_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    return primes


def is_t_prime(x, primes_set):
    root = int(math.isqrt(x))
    if root * root != x:
        return False
    return root in primes_set


def main():

    n = int(input())
    s = list(map(int, input().split()))

    max_num = 10 ** 6
    primes = euler_sieve(max_num)
    primes_set = set(primes)

    results = []
    for num in s:
        if is_t_prime(num, primes_set):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

###通过询问gpt学到了用euler筛判断某个数是否为质数的情形，同时学习到了先存储质数集合然后在逐一对给出的数进行判断的方法，防止超时
