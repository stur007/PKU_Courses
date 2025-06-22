def monkey_king(series,times):
    serial_numbers= []
    for serial_number in series:
        serial_numbers.append(serial_number)
    while len(serial_numbers) >1 :
        for _ in range(times - 1):
            serial_numbers.append(serial_numbers.pop(0))
        serial_numbers.pop(0)
    return serial_numbers.pop(0)
while True:
    n, m = [int(x) for x in input().split()]
    if (n,m) == (0,0):
        break
    else:
        series = [i for i in range(1,n+1)]
        print(monkey_king(series, m))
