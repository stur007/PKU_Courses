s = input()
pre = []
suf = []
i = 0
while True:
    if s[i] == '[':
        temp_num = ''
        temp_alpha = ''
        i += 1
        while True:
            if not s[i].isnumeric():
                temp_num += s[i]
                i += 1
            elif s[i].isalpha():
                temp_alpha += s[i]
                i += 1
            else:
                temp_num = int(temp_num)
                pre.append([temp_num, temp_alpha])
                break

    elif s[i] == ']':
            i += 1
            temp_alpha = ''
            while True:
                if s[i].isalpha():
                    temp_alpha += s[i]
                    i += 1
                else:
                    
