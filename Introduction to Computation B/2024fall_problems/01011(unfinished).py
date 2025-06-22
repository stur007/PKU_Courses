while True:
    n = int(input())
    if n == 0:
        break
    s= list(map(int,input().split()))
    s.sort(reverse = True)
    tot_length = sum(s)
    ans = []
    for i in range(1, tot_length+1):
        if tot_length % i == 0:
            ans.append(i)
    for i in ans:
        collection = []
        for j in s:
            if j > i:
                break
            flag = 0
            for c in collection:
                if c+j <= i:
                    c += j
                    flag = 1
                    break
            if not flag:
                collection.append(j)
        if len(collection) == tot_length//i:
            print(i)
            break