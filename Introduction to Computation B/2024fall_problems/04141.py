n = [int(x) for x in input().split()]
numbers = []
for i_1 in range(n[0]+1):
    for i_2 in range(n[1]+1):
        for i_3 in range(n[2]+1):
            for i_4 in range(n[3]+1):
                for i_5 in range(n[4]+1):
                    for i_6 in range(n[5]+1):
                        numbers.append(i_1 + 2*i_2 +3*i_3 + 5*i_4 + 10*i_5 + 20*i_6)
print('Total='+str(len(set(numbers))-1))