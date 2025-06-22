c = int(input())
for i in range(c):
    print(f'Case {i+1}:')
    n,m,k = map(int,input().split())
    friends = [[] for _ in range(n+1)]
    for _ in range(m):
        i,j = map(int, input().split())
        friends[i].append(j)
        friends[j].append(i)
    for _ in range(k):
        i,j = map(int, input().split())
        print(len(set(friends[i])&set(friends[j])))
##注意[[]]*n创建的是n个索引相同的列表！！！