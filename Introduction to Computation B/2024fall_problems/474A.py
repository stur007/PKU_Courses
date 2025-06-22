command=input()
keyboard=['qwertyuiop','asdfghjkl;','zxcvbnm,./']
s = input()
p=''
if command=='R':
    num=-1
else:
    num=1

for char in s:
    for row in keyboard:
        if char in row:
            p+=row[row.index(char)+num]
            break
print(p)