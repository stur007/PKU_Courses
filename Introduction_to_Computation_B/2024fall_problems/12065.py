x = 5
while True:
    f_x = x ** 3 - 5 * x ** 2 + 10 * x - 80
    f_prime_x = 3 * x ** 2 - 10 * x + 10

    s = x - f_x / f_prime_x

    if abs(x - s) < 10 ** (-10):
        break

    x = s

print(f'{x:.9f}')
