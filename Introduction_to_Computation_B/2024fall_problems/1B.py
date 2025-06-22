t = int(input())
for _ in range(t):
    s = input()
    chars =[]
    for char in s :
        chars.append(char)
    if 'R' in chars and 'C' in chars and chars.index('R') != chars.index('C') - 1:
        row_number = ''.join(chars[chars.index('R')+1: chars.index('C')])
        column_number = int(''.join(chars[chars.index('C')+1:]))
        letter_format =[]
        column_number -= 1
        while column_number > 0 :
            letter = chr(column_number % 26 +65)
            letter_format.append(letter)
            if (column_number + 1) % 26 != 0:
                column_number = column_number // 26
            column_number -= 1
        letter_format.reverse()
        column_number = ''.join(letter_format)
        print(column_number + row_number)

    else:
        number_format = []
        row_number_char = []
        for char in chars :
            if ord(char) > 64:
                number_format.append(char)
            else:
                row_number_char.append(char)
        row_number = ''.join(row_number_char)
        number_format.reverse()
        column_number = 0
        for i, char in enumerate(number_format):
            column_number += (ord(char) - 64) * (26 ** i)

        print('R' + row_number + 'C' +str(column_number))