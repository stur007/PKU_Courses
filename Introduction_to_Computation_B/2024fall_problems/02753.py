numbers =[1,1]
for _ in range(18):
    numbers.append(numbers[-1] + numbers[-2])
n = int(input())
for _ in range(n):
    print(numbers[int(input())-1])