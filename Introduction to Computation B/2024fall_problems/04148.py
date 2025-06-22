cnt = 0
while True:
    cnt += 1
    p, e, i, d =[int(x) for x in input().split()]
    if (p,e,i,d) == (-1,-1,-1,-1):
        break
    list_p = [p+j*23 for j in range(int(21252/23)+d+1)]
    list_e = [e+j*28 for j in range(int(21252/28)+d+1)]
    list_i = [i+j*33 for j in range(int(21252/33)+d+1)]
    answers = list(set(list_p)&set(list_e)&set(list_i))
    answers.sort()
    while answers[0] <= d:
        answers.pop(0)
    ans = answers[0]-d
    print('Case '+str(cnt)+': the next triple peak occurs in '+str(ans)+' days.')