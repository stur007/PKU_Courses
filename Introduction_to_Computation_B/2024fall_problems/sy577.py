s = input()
max_length = 1
length = 1
i = 0
while i < len(s) - 1:
    if s[i] == '0':
        if s[i+1] == '1':
            length += 1
            i += 1
        else:
            max_length = max(max_length, length)
            length = 1
            i += 1
    else:
        if s[i+1] == '0':
            length += 1
            i += 1
        else:
            max_length = max(max_length, length)
            length = 1
            i += 1
    max_length = max(max_length, length)
print(max_length)