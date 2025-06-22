s = input()
vowels='aoyeui'
ans = ''
for letter in s:
    letter=letter.lower()
    if not letter in vowels :
        ans+='.'+letter
print(ans)