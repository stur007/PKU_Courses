numbers=[int(x) for x in input().split()]
numbers.sort(reverse=True)
answer=[]
for i in range(1,4):
    answer.append(numbers[0]-numbers[i])
print(*answer,sep=' ')


