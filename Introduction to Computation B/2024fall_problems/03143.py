def is_prime(n):
    prime_set = []
    for i in range(2, n+1):
        case = True
        for j in range(2, int(i ** 0.5)+1):
            if i %j == 0:
                case = False
                break
        if case:
            prime_set.append(i)
    return prime_set
prime_numbers = is_prime(2000)
x = int(input())
if x % 2 == 1 or x < 6:
    print('Error!')
else:
    for num in prime_numbers:
        if num > x/2 :
            break
        else:
            if x - num in prime_numbers:
                print(str(x)+'='+str(num)+'+'+str(x-num))
