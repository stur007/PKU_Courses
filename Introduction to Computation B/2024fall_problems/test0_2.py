#初学者生成的代码
string = input()
result = []
for char in string:
    if char==char.lower():
        result.append(char.upper())
    elif char==char.upper():
        result.append(char.lower())
    else:
        result.append(char)
print(''.join(result))

#ChatGPT是生成的代码
def swap_case(s):
    return s.swapcase()

# 读取输入
input_string = input().strip()

# 调用函数并输出结果
output_string = swap_case(input_string)
print(output_string)
