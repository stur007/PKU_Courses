n = int(input())
words = input().split()
article = []
current_line = ''

for word in words:
    if len(current_line) + len(word) + (1 if current_line else 0) > 80:
        article.append(current_line.strip())
        current_line = word
    else:
        if current_line:
            current_line += ' ' + word
        else:
            current_line = word

article.append(current_line.strip())
print(*article, sep='\n')
