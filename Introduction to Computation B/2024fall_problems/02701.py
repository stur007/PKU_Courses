n = int(input())
numbers = []
for i in range(n + 1):
    if i % 7 == 0 :
        continue
    if '7' in str(i) :
        continue
    numbers.append(i)
print(sum(x**2 for x in numbers))
