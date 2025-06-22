while True:
    try:
        s = input()
        flag = 1
    except EOFError:
        break
    if s[0]=='@' or s[0] == '.' or s[-1] == '@' or s[-1] =='.':
        flag = 0
    else:
        cnt_at = 0
        for i in range(len(s)):
            if s[i] == '@':
                cnt_at += 1
                index_at = i
        if cnt_at ==1:
            if s[index_at-1] =='.' or s[index_at+1] == '.':
                flag = 0
            else:
                cnt_dot = 0
                for j in range(index_at+1,len(s)):
                    if s[j] == '.':
                        cnt_dot +=1
                if cnt_dot >= 1:
                    flag = 1
                else:
                    flag = 0
        else:
            flag = 0

    if flag == 0:
        print('NO')
    else:
        print('YES')
#注意读题，此题的坑点在于有可能出现.@的情形。